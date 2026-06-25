"""
WO Schedule — standalone replication of EVO WO-L-B
Filter form mirrors T7WOLB.DFM; report mirrors T6WOLB2.RTM (ISTS Enhanced)
Database: DSN=DBA (Pervasive SQL)
"""

import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import pyodbc
from datetime import datetime, date
import os
import sys
import tempfile
import subprocess
import configparser

from reportlab.lib.pagesizes import landscape, letter
from reportlab.lib.units import inch, mm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_RIGHT, TA_LEFT

# ---------------------------------------------------------------------------
# Config — DSN name stored in wo-schedule.ini next to the EXE
# ---------------------------------------------------------------------------

def _config_path():
    base = os.path.dirname(sys.executable if getattr(sys, "frozen", False) else os.path.abspath(__file__))
    return os.path.join(base, "wo-schedule.ini")

def _load_dsn():
    cfg = configparser.ConfigParser()
    cfg.read(_config_path())
    return cfg.get("database", "dsn", fallback="DBA")

def _save_dsn(dsn):
    cfg = configparser.ConfigParser()
    cfg["database"] = {"dsn": dsn}
    with open(_config_path(), "w") as f:
        cfg.write(f)

DSN = _load_dsn()

# ---------------------------------------------------------------------------
# Database helpers
# ---------------------------------------------------------------------------

def get_conn():
    return pyodbc.connect(f"DSN={DSN}", autocommit=True)


def get_company_name():
    try:
        with get_conn() as cn:
            row = cn.execute("SELECT BKSY_COMP_NAME FROM BKSYMSTR").fetchone()
            return row[0].strip() if row else "ISTS"
    except Exception:
        return "ISTS"


def fmt_date(val):
    if val is None:
        return ""
    if isinstance(val, (datetime, date)):
        return val.strftime("%m/%d/%Y")
    return str(val).strip()


def fmt_num(val, decimals=0):
    if val is None:
        return ""
    try:
        f = float(val)
        if decimals == 0:
            return f"{f:,.0f}"
        return f"{f:,.{decimals}f}"
    except Exception:
        return str(val).strip()


# ---------------------------------------------------------------------------
# Query builder
# ---------------------------------------------------------------------------

def build_and_run(filters):
    """Execute the WO query and return list of row dicts."""
    wheres = []
    params = []

    # Status filter — must match at least one checked box
    status_vals = []
    for code, checked in [('S', filters['st_sched']), ('F', filters['st_firm']),
                           ('R', filters['st_rel']),  ('C', filters['st_closed'])]:
        if checked:
            status_vals.append(code)
    if status_vals:
        placeholders = ",".join("?" * len(status_vals))
        wheres.append(f"w.MTWO_WIP_STATUS IN ({placeholders})")
        params.extend(status_vals)

    def _is_blank_date(s):
        return not s or s.strip() in ("", "00/00/00", "0/0/0", "00/00/0000")

    # Date ranges
    def add_date_range(col, frm, thru):
        if frm and not _is_blank_date(frm):
            try:
                wheres.append(f"w.{col} >= ?")
                params.append(datetime.strptime(frm.strip(), "%m/%d/%Y"))
            except ValueError:
                pass
        if thru and not _is_blank_date(thru):
            try:
                wheres.append(f"w.{col} <= ?")
                params.append(datetime.strptime(thru.strip(), "%m/%d/%Y"))
            except ValueError:
                pass

    add_date_range("MTWO_WIP_SSTART", filters['from_sstart'], filters['thru_sstart'])
    add_date_range("MTWO_WIP_SFIN",   filters['from_sfin'],   filters['thru_sfin'])
    add_date_range("MTWO_WIP_DDATE",  filters['from_ddate'],  filters['thru_ddate'])

    # WO number range (format: "1234" or "1234-5"; spaces are stripped everywhere)
    def parse_wonum(s):
        s = s.replace(" ", "").strip()
        if not s:
            return None, None
        parts = s.split("-", 1)
        pre = parts[0].strip()
        suf = parts[1].strip() if len(parts) > 1 else None
        return pre, suf

    f_pre, f_suf = parse_wonum(filters['from_wo'])
    t_pre, t_suf = parse_wonum(filters['thru_wo'])
    if f_pre:
        wheres.append("w.MTWO_WIP_WOPRE >= ?")
        params.append(f_pre)
    if t_pre:
        wheres.append("w.MTWO_WIP_WOPRE <= ?")
        params.append(t_pre)

    # Text range filters (spaces stripped before comparison)
    def add_str_range(col, frm, thru):
        if frm:
            wheres.append(f"w.{col} >= ?")
            params.append(frm.replace(" ", "").strip().upper())
        if thru:
            wheres.append(f"w.{col} <= ?")
            params.append(thru.replace(" ", "").strip().upper())

    add_str_range("MTWO_WIP_CODE",   filters['from_item'],   filters['thru_item'])
    add_str_range("MTWO_CUSTCODE",   filters['from_cust'],   filters['thru_cust'])
    add_str_range("MTWO_WIP_CUSORD", filters['from_cusord'], filters['thru_cusord'])
    add_str_range("MTWO_WIP_PROJ",   filters['from_plan'],   filters['thru_plan'])
    add_str_range("MTWO_WIP_SONUM",  filters['from_so'],     filters['thru_so'])

    # SO-only / orphans-only
    if filters['so_only']:
        wheres.append("LTRIM(RTRIM(w.MTWO_WIP_SONUM)) <> ''")
    if filters['orphans_only']:
        wheres.append("(LTRIM(RTRIM(w.MTWO_WIP_SONUM)) = '' OR w.MTWO_WIP_SONUM IS NULL)")

    # Class code filter (against BKICMSTR.BKIC_PROD_CLASS via existing LEFT JOIN)
    if not filters['all_class']:
        codes = [c for c in filters['class_codes'] if c]
        if codes or not filters['blank_class']:
            parts = []
            if codes:
                placeholders = ",".join("?" * len(codes))
                parts.append(f"i.BKIC_PROD_CLASS IN ({placeholders})")
                params.extend(codes)
            if filters['blank_class']:
                parts.append("(i.BKIC_PROD_CLASS IS NULL OR LTRIM(RTRIM(i.BKIC_PROD_CLASS)) = '')")
            if parts:
                wheres.append("(" + " OR ".join(parts) + ")")

    where_sql = ("WHERE " + " AND ".join(wheres)) if wheres else ""

    # Sort
    sort_map = {
        "1 - Start Date":   "w.MTWO_WIP_SSTART, w.MTWO_WIP_WOPRE, w.MTWO_WIP_WOSUF",
        "2 - Finish Date":  "w.MTWO_WIP_SFIN, w.MTWO_WIP_WOPRE, w.MTWO_WIP_WOSUF",
        "3 - Work Order":   "w.MTWO_WIP_WOPRE, w.MTWO_WIP_WOSUF",
        "4 - Item Number":  "w.MTWO_WIP_CODE, w.MTWO_WIP_WOPRE, w.MTWO_WIP_WOSUF",
        "5 - Customer":     "w.MTWO_CUSTCODE, w.MTWO_WIP_WOPRE, w.MTWO_WIP_WOSUF",
        "6 - Job Number":   "w.MTWO_WIP_PROJ, w.MTWO_WIP_WOPRE, w.MTWO_WIP_WOSUF",
        "7 - Due Date":     "w.MTWO_WIP_DDATE, w.MTWO_WIP_WOPRE, w.MTWO_WIP_WOSUF",
        "8 - SO Number":    "w.MTWO_WIP_SONUM, w.MTWO_WIP_WOPRE, w.MTWO_WIP_WOSUF",
    }
    order = sort_map.get(filters['sort_by'], "w.MTWO_WIP_SFIN, w.MTWO_WIP_WOPRE, w.MTWO_WIP_WOSUF")

    sql = f"""
        SELECT
            w.MTWO_WIP_WOPRE, w.MTWO_WIP_WOSUF, w.MTWO_WIP_CODE,
            w.MTWO_WIP_STATUS, w.MTWO_WIP_PRTY, w.MTWO_WIP_USERCD,
            w.MTWO_WIP_SSTART, w.MTWO_WIP_SFIN, w.MTWO_WIP_DDATE,
            w.MTWO_WIP_SQTY, w.MTWO_WIP_COMQTY,
            w.MTWO_WIP_ASTART, w.MTWO_WIP_AFIN,
            w.MTWO_WIP_PPRCE, w.MTWO_WIP_LOC,
            w.MTWO_CUSTCODE, w.MTWO_CUSTNAME,
            w.MTWO_WIP_SONUM,
            i.BKIC_PROD_DESC, i.BKIC_PROD_CLASS
        FROM WORKORD w
        LEFT JOIN BKICMSTR i ON w.MTWO_WIP_CODE = i.BKIC_PROD_CODE
        {where_sql}
        ORDER BY {order}
    """

    rows = []
    with get_conn() as cn:
        cursor = cn.execute(sql, params)
        cols = [d[0] for d in cursor.description]
        for r in cursor.fetchall():
            rows.append(dict(zip(cols, r)))

    # --- Unstarted WOs filter (past sstart, no labor) ---
    if filters['unstarted_only'] and rows:
        wo_keys = set((r['MTWO_WIP_WOPRE'], r['MTWO_WIP_WOSUF']) for r in rows)
        with get_conn() as cn:
            labor_sql = "SELECT DISTINCT MTWOLA_WOPRE, MTWOLA_WOSUF FROM WOLABOR"
            has_labor = set()
            for lr in cn.execute(labor_sql).fetchall():
                has_labor.add((str(lr[0]).strip(), str(lr[1]).strip()))
        today = datetime.now()
        rows = [
            r for r in rows
            if (r['MTWO_WIP_SSTART'] and r['MTWO_WIP_SSTART'] <= today)
            and (r['MTWO_WIP_WOPRE'].strip(), r['MTWO_WIP_WOSUF'].strip()) not in has_labor
        ]

    # --- Last operation lookup ---
    last_op_mode = filters['last_op_mode'].strip().upper()
    if last_op_mode and last_op_mode != 'N' and rows:
        wo_keys_list = list(set(
            (r['MTWO_WIP_WOPRE'].strip(), r['MTWO_WIP_WOSUF'].strip()) for r in rows
        ))
        routing_map = {}
        with get_conn() as cn:
            ro_sql = """
                SELECT MTWORO_WOPRE, MTWORO_WOSUF, MTWORO_OPER,
                       MTWORO_OPERDESC, MTWORO_QTYCOM, MTWORO_STQTY, MTWORO_STARTED
                FROM WOROUT
                ORDER BY MTWORO_WOPRE, MTWORO_WOSUF, MTWORO_OPER
            """
            for ro in cn.execute(ro_sql).fetchall():
                key = (str(ro[0]).strip(), str(ro[1]).strip())
                if key not in routing_map:
                    routing_map[key] = []
                routing_map[key].append({
                    'oper': ro[2], 'desc': str(ro[3]).strip(),
                    'qtycom': ro[4] or 0, 'stqty': ro[5] or 0,
                    'started': ro[6]
                })

        for r in rows:
            key = (r['MTWO_WIP_WOPRE'].strip(), r['MTWO_WIP_WOSUF'].strip())
            ops = routing_map.get(key, [])
            sqty = float(r['MTWO_WIP_SQTY'] or 0)
            last = None
            for op in ops:
                qtycom = float(op['qtycom'])
                stqty  = float(op['stqty'])
                qualifies = False
                if last_op_mode == 'C':
                    qualifies = sqty > 0 and qtycom >= sqty
                elif last_op_mode == 'Q':
                    qualifies = qtycom > 0
                elif last_op_mode == 'A':
                    qualifies = op['started'] is not None
                elif last_op_mode == 'S':
                    qualifies = stqty > 0
                if qualifies:
                    last = op
            r['_last_op']     = last['oper']    if last else ""
            r['_last_op_desc']= last['desc']    if last else ""
            r['_qty_thru_op'] = fmt_num(last['qtycom']) if last else ""
        else:
            pass
    else:
        for r in rows:
            r['_last_op'] = r['_last_op_desc'] = r['_qty_thru_op'] = ""

    return rows


# ---------------------------------------------------------------------------
# PDF report — mirrors T6WOLB2.RTM landscape layout
# ---------------------------------------------------------------------------

REPORT_COLS = [
    # (header line1, header line2, field_fn, width_in, align)
    # Column order matches EVO T6WOLB2.RTM (ISTS Enhanced): WO, Item#, Desc, Qty, CmpQty, S, P, C, Start, Finish, CustCode, CustName, Due, ActStart, ActFinish, LastOper, QtyThruOp, PriceExt
    ("Work",    "Order",       lambda r: f"{r['MTWO_WIP_WOPRE'].strip()}-{r['MTWO_WIP_WOSUF'].strip()}", 0.65, 'L'),
    ("Item",    "Number",      lambda r: r['MTWO_WIP_CODE'].strip(),                                      0.80, 'L'),
    ("Item",    "Description", lambda r: (r['BKIC_PROD_DESC'] or '').strip(),                             1.00, 'L'),
    ("Sched",   "Qty",         lambda r: fmt_num(r['MTWO_WIP_SQTY']),                                     0.48, 'R'),
    ("Compl",   "Qty",         lambda r: fmt_num(r['MTWO_WIP_COMQTY']),                                   0.48, 'R'),
    ("S",       "",            lambda r: r['MTWO_WIP_STATUS'].strip(),                                    0.15, 'C'),
    ("P",       "",            lambda r: str(r['MTWO_WIP_PRTY'] or '').strip(),                           0.13, 'C'),
    ("C",       "",            lambda r: str(r['MTWO_WIP_USERCD'] or '').strip(),                         0.18, 'C'),
    ("Start",   "Schedule",    lambda r: fmt_date(r['MTWO_WIP_SSTART']),                                  0.68, 'C'),
    ("Finish",  "Schedule",    lambda r: fmt_date(r['MTWO_WIP_SFIN']),                                    0.68, 'C'),
    ("Cust",    "Code",        lambda r: r['MTWO_CUSTCODE'].strip() if r['MTWO_CUSTCODE'] else '',        0.55, 'L'),
    ("Cust",    "Name",        lambda r: r['MTWO_CUSTNAME'].strip() if r['MTWO_CUSTNAME'] else '',        0.90, 'L'),
    ("Due",     "Date",        lambda r: fmt_date(r['MTWO_WIP_DDATE']),                                   0.68, 'C'),
    ("Actual",  "Start",       lambda r: fmt_date(r['MTWO_WIP_ASTART']),                                  0.68, 'C'),
    ("Actual",  "Finish",      lambda r: fmt_date(r['MTWO_WIP_AFIN']),                                    0.68, 'C'),
    ("Last",    "Oper",        lambda r: r.get('_last_op', ''),                                           0.35, 'C'),
    ("Qty thru","Op",          lambda r: r.get('_qty_thru_op', ''),                                       0.45, 'R'),
    ("Price",   "Ext",         lambda r: fmt_num(float(r['MTWO_WIP_PPRCE'] or 0) * float(r['MTWO_WIP_SQTY'] or 0), 2), 0.68, 'R'),
]

ALIGN_MAP = {'L': TA_LEFT, 'C': TA_CENTER, 'R': TA_RIGHT}


def generate_pdf(rows, filters, company_name, out_path):
    page = landscape(letter)
    pw, ph = page
    margin = 0.3 * inch

    print_date = datetime.now().strftime("%m/%d/%Y")

    # --- canvas callback: date top-left, page number top-right ---
    def _draw_page(canvas, doc):
        canvas.saveState()
        canvas.setFont("Helvetica", 7)
        canvas.drawString(margin, ph - margin + 4, print_date)
        canvas.drawRightString(pw - margin, ph - margin + 4, f"Page: {doc.page}")
        canvas.restoreState()

    doc = SimpleDocTemplate(
        out_path,
        pagesize=page,
        leftMargin=margin, rightMargin=margin,
        topMargin=margin + 10, bottomMargin=margin,
    )

    bold_c  = ParagraphStyle('bold_c',  fontName='Helvetica-Bold', fontSize=9, alignment=TA_CENTER)
    crit_b  = ParagraphStyle('crit_b',  fontName='Helvetica-Bold', fontSize=7, alignment=TA_LEFT)
    crit_n  = ParagraphStyle('crit_n',  fontName='Helvetica',      fontSize=7, alignment=TA_LEFT)
    foot_s  = ParagraphStyle('foot_s',  fontName='Helvetica',      fontSize=6, alignment=TA_LEFT)

    story = []

    # Title
    story.append(Paragraph("WORK ORDER SCHEDULE", bold_c))
    story.append(Spacer(1, 4))

    # --- Criteria block (3-column table matching EVO layout) ---
    def _cr(label, val):
        return Paragraph(f"<b>{label}</b> {val}", crit_n)

    def _rng(label, frm, thru):
        f = frm if frm else ""
        t = thru if thru else ""
        return Paragraph(f"<b>{label}</b>  From  {f}    Thru  {t}", crit_n)

    statuses = "".join(c for c, chk in [('S', filters['st_sched']), ('F', filters['st_firm']),
                                         ('R', filters['st_rel']),   ('C', filters['st_closed'])] if chk)
    classes = " ".join(c for c in filters['class_codes'] if c)
    class_label = "All" if filters['all_class'] else (classes + " only" if classes else "None")

    left = [
        _rng("Item",        filters['from_item'],   filters['thru_item']),
        _rng("WO",          filters['from_wo'],     filters['thru_wo']),
        _cr("WO Status",    statuses),
        _cr("WO Priority",  ""),
        _cr("Class codes",  class_label),
    ]
    mid = [
        _rng("Cust",        filters['from_cust'],   filters['thru_cust']),
        _rng("Cust PO",     filters['from_cusord'], filters['thru_cusord']),
        _rng("Start Date",  filters['from_sstart'], filters['thru_sstart']),
        _rng("Fin Date",    filters['from_sfin'],   filters['thru_sfin']),
        _rng("SO",          filters['from_so'],     filters['thru_so']),
    ]
    right = [
        _rng("Plan",        filters['from_plan'],   filters['thru_plan']),
        _rng("Job",         filters['from_job'],    filters['thru_job']),
        Paragraph(f"<b>Sort:</b> {filters['sort_by']}", crit_n),
        Paragraph("", crit_n),
        Paragraph("", crit_n),
    ]

    usable_w = pw - 2 * margin
    crit_col = usable_w / 3
    crit_rows = list(zip(left, mid, right))
    crit_tbl = Table(crit_rows, colWidths=[crit_col, crit_col, crit_col])
    crit_tbl.setStyle(TableStyle([
        ('VALIGN',       (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING',   (0,0), (-1,-1), 1),
        ('BOTTOMPADDING',(0,0), (-1,-1), 1),
        ('LEFTPADDING',  (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(crit_tbl)
    story.append(Spacer(1, 6))

    # --- Data table ---
    col_widths = [c[3] * inch for c in REPORT_COLS]

    def hcell(txt):
        return Paragraph(f"<b>{txt}</b>", ParagraphStyle('hdr', fontName='Helvetica-Bold',
                         fontSize=5.5, alignment=TA_CENTER))

    table_data = [
        [hcell(c[0]) for c in REPORT_COLS],
        [hcell(c[1]) for c in REPORT_COLS],
    ]

    for r in rows:
        row_cells = []
        for col in REPORT_COLS:
            try:
                val = col[2](r)
            except Exception:
                val = ""
            align = ALIGN_MAP.get(col[4], TA_LEFT)
            row_cells.append(
                Paragraph(str(val), ParagraphStyle('cell', fontName='Helvetica',
                           fontSize=6.5, alignment=align))
            )
        table_data.append(row_cells)

    tbl = Table(table_data, colWidths=col_widths, repeatRows=2)
    tbl.setStyle(TableStyle([
        ('BACKGROUND',     (0,0), (-1,1), colors.HexColor('#D0D0D0')),
        ('LINEBELOW',      (0,1), (-1,1), 0.5, colors.black),
        ('LINEBELOW',      (0,2), (-1,-1), 0.25, colors.HexColor('#CCCCCC')),
        ('VALIGN',         (0,0), (-1,-1), 'MIDDLE'),
        ('ROWBACKGROUNDS', (0,2), (-1,-1), [colors.white, colors.HexColor('#F5F5F5')]),
        ('TOPPADDING',     (0,0), (-1,-1), 2),
        ('BOTTOMPADDING',  (0,0), (-1,-1), 2),
        ('LEFTPADDING',    (0,0), (-1,-1), 2),
        ('RIGHTPADDING',   (0,0), (-1,-1), 2),
    ]))
    story.append(tbl)

    story.append(Spacer(1, 6))
    story.append(Paragraph(f"{len(rows)} work order(s)", foot_s))

    doc.build(story, onFirstPage=_draw_page, onLaterPages=_draw_page)


# ---------------------------------------------------------------------------
# Filter form — mirrors T7WOLB.DFM layout
# ---------------------------------------------------------------------------

SORT_OPTIONS = [
    "1 - Start Date",
    "2 - Finish Date",
    "3 - Work Order",
    "4 - Item Number",
    "5 - Customer",
    "6 - Job Number",
    "7 - Due Date",
    "8 - SO Number",
]


# ---------------------------------------------------------------------------
# Search dialog + fetchers
# ---------------------------------------------------------------------------

def _fetch_wo():
    with get_conn() as cn:
        rows = cn.execute(
            "SELECT MTWO_WIP_WOPRE, MTWO_WIP_WOSUF FROM WORKORD ORDER BY MTWO_WIP_WOPRE, MTWO_WIP_WOSUF"
        ).fetchall()
    result = []
    for r in rows:
        pre = str(r[0]).strip(); suf = str(r[1]).strip()
        key = f"{pre}-{suf}"
        result.append((key, key))
    return result

def _fetch_item():
    with get_conn() as cn:
        rows = cn.execute(
            "SELECT BKIC_PROD_CODE, BKIC_PROD_DESC FROM BKICMSTR ORDER BY BKIC_PROD_CODE"
        ).fetchall()
    return [(str(r[0]).strip(), f"{str(r[0]).strip():<20} {str(r[1] or '').strip()}") for r in rows]

def _fetch_cust():
    with get_conn() as cn:
        rows = cn.execute(
            "SELECT DISTINCT MTWO_CUSTCODE, MTWO_CUSTNAME FROM WORKORD "
            "WHERE LTRIM(RTRIM(MTWO_CUSTCODE)) <> '' ORDER BY MTWO_CUSTCODE"
        ).fetchall()
    return [(str(r[0]).strip(), f"{str(r[0]).strip():<12} {str(r[1] or '').strip()}") for r in rows]

def _fetch_distinct(table, col, label_col=None):
    with get_conn() as cn:
        if label_col:
            rows = cn.execute(
                f"SELECT DISTINCT {col}, {label_col} FROM {table} "
                f"WHERE LTRIM(RTRIM({col})) <> '' ORDER BY {col}"
            ).fetchall()
            return [(str(r[0]).strip(), f"{str(r[0]).strip():<16} {str(r[1] or '').strip()}") for r in rows]
        else:
            rows = cn.execute(
                f"SELECT DISTINCT {col} FROM {table} "
                f"WHERE LTRIM(RTRIM({col})) <> '' ORDER BY {col}"
            ).fetchall()
            return [(str(r[0]).strip(), str(r[0]).strip()) for r in rows]


def _build_wo_query_for_search(filters):
    """Run a lightweight WO query applying only status+class filters (for filter-aware search)."""
    wheres = []
    params = []

    status_vals = [c for c, chk in [('S', filters['st_sched']), ('F', filters['st_firm']),
                                     ('R', filters['st_rel']),  ('C', filters['st_closed'])] if chk]
    if status_vals:
        wheres.append(f"w.MTWO_WIP_STATUS IN ({','.join('?'*len(status_vals))})")
        params.extend(status_vals)

    if not filters['all_class']:
        codes = [c for c in filters['class_codes'] if c]
        parts = []
        if codes:
            parts.append(f"i.BKIC_PROD_CLASS IN ({','.join('?'*len(codes))})")
            params.extend(codes)
        if filters['blank_class']:
            parts.append("(i.BKIC_PROD_CLASS IS NULL OR LTRIM(RTRIM(i.BKIC_PROD_CLASS))='')")
        if parts:
            wheres.append("(" + " OR ".join(parts) + ")")

    where_sql = ("WHERE " + " AND ".join(wheres)) if wheres else ""
    sql = (f"SELECT w.MTWO_WIP_WOPRE, w.MTWO_WIP_WOSUF, w.MTWO_WIP_CODE, "
           f"w.MTWO_CUSTCODE, w.MTWO_CUSTNAME "
           f"FROM WORKORD w "
           f"LEFT JOIN BKICMSTR i ON w.MTWO_WIP_CODE = i.BKIC_PROD_CODE "
           f"{where_sql} ORDER BY w.MTWO_WIP_WOPRE, w.MTWO_WIP_WOSUF")
    with get_conn() as cn:
        return cn.execute(sql, params).fetchall()


def _fetch_wo_filtered(filters):
    rows = _build_wo_query_for_search(filters)
    result = []
    for r in rows:
        key = f"{str(r[0]).strip()}-{str(r[1]).strip()}"
        result.append((key, key))
    return result

def _fetch_item_filtered(filters):
    rows = _build_wo_query_for_search(filters)
    codes = sorted({str(r[2]).strip() for r in rows if r[2] and str(r[2]).strip()})
    with get_conn() as cn:
        result = []
        for code in codes:
            desc_row = cn.execute("SELECT BKIC_PROD_DESC FROM BKICMSTR WHERE BKIC_PROD_CODE=?", (code,)).fetchone()
            d = str(desc_row[0]).strip() if desc_row else ""
            result.append((code, f"{code:<20} {d}"))
    return result

def _fetch_cust_filtered(filters):
    rows = _build_wo_query_for_search(filters)
    seen = {}
    for r in rows:
        code = str(r[3]).strip() if r[3] else ""
        name = str(r[4]).strip() if r[4] else ""
        if code and code not in seen:
            seen[code] = name
    return [(k, f"{k:<12} {v}") for k, v in sorted(seen.items())]


class SearchDialog(tk.Toplevel):
    """Generic search-and-pick dialog. Fills v_from and v_thru with selected value.

    fetcher()          -> list of (key, display_str) — unfiltered (all records)
    filtered_fetcher() -> list of (key, display_str) — respects current form filters
                         Pass None if no filtered variant is available.
    """

    def __init__(self, parent, title, fetcher, v_from, v_thru, filtered_fetcher=None):
        super().__init__(parent)
        self.title(title)
        self.v_from = v_from
        self.v_thru = v_thru
        self._fetcher          = fetcher
        self._filtered_fetcher = filtered_fetcher
        self._all_rows    = []
        self._current_rows = []

        self.transient(parent)
        self.grab_set()
        self.resizable(True, True)
        self.geometry("480x420")

        FONT    = ("Arial", 9)
        FONT_SM = ("Arial", 8)

        # Search bar
        top = tk.Frame(self)
        top.pack(fill=tk.X, padx=8, pady=(8, 2))
        tk.Label(top, text="Search:", font=FONT).pack(side=tk.LEFT)
        self._v_search = tk.StringVar()
        self._v_search.trace_add("write", self._on_search)
        tk.Entry(top, textvariable=self._v_search, width=30, font=FONT).pack(side=tk.LEFT, padx=4)

        # "Use current filters" toggle — only shown when a filtered_fetcher was supplied
        if filtered_fetcher is not None:
            self._v_use_filter = tk.BooleanVar(value=False)
            tk.Checkbutton(
                top, text="Use current form filters", variable=self._v_use_filter,
                font=("Arial", 8), command=self._reload
            ).pack(side=tk.LEFT, padx=8)
        else:
            self._v_use_filter = None

        # Listbox + scrollbar
        mid = tk.Frame(self)
        mid.pack(fill=tk.BOTH, expand=True, padx=8, pady=4)
        self._lb = tk.Listbox(mid, font=FONT_SM, selectmode=tk.SINGLE)
        sb = tk.Scrollbar(mid, command=self._lb.yview)
        self._lb.config(yscrollcommand=sb.set)
        self._lb.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        sb.pack(side=tk.RIGHT, fill=tk.Y)
        self._lb.bind("<Double-Button-1>", self._select)

        # Status label + buttons
        bot = tk.Frame(self)
        bot.pack(fill=tk.X, padx=8, pady=(0, 8))
        self._lbl_count = tk.Label(bot, text="", font=("Arial", 7), fg="gray")
        self._lbl_count.pack(side=tk.LEFT)
        tk.Button(bot, text="Select", width=10, font=FONT, command=self._select).pack(side=tk.RIGHT, padx=4)
        tk.Button(bot, text="Cancel", width=10, font=FONT, command=self.destroy).pack(side=tk.RIGHT)

        self._reload()
        self.wait_window()

    def _reload(self):
        use_filtered = self._v_use_filter is not None and self._v_use_filter.get()
        fn = self._filtered_fetcher if use_filtered else self._fetcher
        self.config(cursor="watch"); self.update()
        try:
            self._all_rows = fn()
        except Exception as ex:
            messagebox.showerror("Search Error", str(ex), parent=self)
            self._all_rows = []
        self.config(cursor="")
        self._v_search.set("")
        self._populate(self._all_rows)

    def _populate(self, rows):
        self._lb.delete(0, tk.END)
        self._current_rows = rows
        for _, display in rows:
            self._lb.insert(tk.END, display)
        self._lbl_count.config(text=f"{len(rows)} record(s)")

    def _on_search(self, *_):
        term = self._v_search.get().strip().upper()
        self._populate(
            [(k, d) for k, d in self._all_rows if term in d.upper()] if term else self._all_rows
        )

    def _select(self, event=None):
        sel = self._lb.curselection()
        if not sel:
            return
        key, _ = self._current_rows[sel[0]]
        self.v_from.set(key)
        self.v_thru.set(key)
        self.destroy()


class WOScheduleApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("WO-L-B  Print Work Order Schedule — ISTS")
        self.resizable(False, False)
        self._build_ui()
        self.company_name = get_company_name()

    # ---- UI construction ----

    def _build_ui(self):
        FONT      = ("Arial", 9)
        FONT_BOLD = ("Arial", 9, "bold")
        FONT_SM   = ("Arial", 8)

        outer = tk.Frame(self, bd=2, relief=tk.SUNKEN)
        outer.pack(fill=tk.BOTH, expand=True, padx=4, pady=4)

        # ---- top toolbar row ----
        top = tk.Frame(outer)
        top.pack(fill=tk.X, pady=(4, 0))

        tk.Label(top, text="Sort Report By", font=FONT).pack(side=tk.LEFT, padx=(8, 4))
        self.v_sort = tk.StringVar(value=SORT_OPTIONS[0])
        ttk.Combobox(top, textvariable=self.v_sort, values=SORT_OPTIONS,
                     state="readonly", width=18, font=FONT).pack(side=tk.LEFT)

        # ---- main body: left panel + right panel ----
        body = tk.Frame(outer)
        body.pack(fill=tk.BOTH, expand=True, padx=4, pady=4)

        left  = tk.Frame(body, width=290)
        left.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 8))
        left.pack_propagate(False)

        right = tk.Frame(body)
        right.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self._build_left(left, FONT, FONT_BOLD, FONT_SM)
        self._build_right(right, FONT, FONT_BOLD)

        # ---- bottom button bar ----
        bar = tk.Frame(outer, bd=1, relief=tk.SUNKEN)
        bar.pack(fill=tk.X, side=tk.BOTTOM, pady=(4, 0))
        tk.Button(bar, text="&Print", width=10, font=FONT, command=self._on_print).pack(side=tk.RIGHT, padx=4, pady=4)
        tk.Button(bar, text="E&xit",  width=10, font=FONT, command=self.destroy).pack(side=tk.RIGHT, padx=4, pady=4)

    def _build_left(self, parent, font, font_bold, font_sm):
        r = 0

        # Bold filter-scope label
        lbl = tk.Label(parent, text="Filter the report to Work Order Range only\ninclude work orders with",
                       font=font_bold, justify=tk.LEFT, wraplength=270)
        lbl.grid(row=r, column=0, columnspan=2, sticky=tk.W, pady=(4, 6)); r += 1

        # STATUS
        tk.Label(parent, text="STATUS", font=font_bold).grid(row=r, column=0, sticky=tk.W); r += 1
        self.v_st_sched  = tk.BooleanVar(value=True)
        self.v_st_firm   = tk.BooleanVar(value=True)
        self.v_st_rel    = tk.BooleanVar(value=True)
        self.v_st_closed = tk.BooleanVar(value=False)
        for label, var in [("Scheduled", self.v_st_sched), ("Firmed", self.v_st_firm),
                            ("Released",  self.v_st_rel),  ("Closed",  self.v_st_closed)]:
            tk.Checkbutton(parent, text=f"  {label}", variable=var, font=font).grid(
                row=r, column=0, columnspan=2, sticky=tk.W); r += 1

        tk.Frame(parent, height=6).grid(row=r, column=0); r += 1

        # WO CLASS
        tk.Label(parent, text="WO CLASS", font=font_bold).grid(row=r, column=0, sticky=tk.W); r += 1
        self.v_all_class = tk.BooleanVar(value=False)
        tk.Checkbutton(parent, text="Include All Class Codes?", variable=self.v_all_class,
                       font=font, command=self._toggle_classes).grid(row=r, column=0, columnspan=2, sticky=tk.W); r += 1

        # 6 class code slots
        tk.Label(parent, text="Included Classes", font=font_sm).grid(row=r, column=0, sticky=tk.W)
        class_frame = tk.Frame(parent)
        class_frame.grid(row=r, column=1, sticky=tk.W); r += 1
        self._class_vars = []
        self._class_entries = []
        _class_defaults = ["W", "B", "", "", "", ""]
        for i in range(6):
            v = tk.StringVar(value=_class_defaults[i])
            e = tk.Entry(class_frame, textvariable=v, width=3, font=font, state=tk.NORMAL)
            e.pack(side=tk.LEFT, padx=1)
            self._class_vars.append(v)
            self._class_entries.append(e)

        self.v_blank_class = tk.BooleanVar(value=False)
        tk.Checkbutton(parent, text="Include Blank Classes?", variable=self.v_blank_class,
                       font=font).grid(row=r, column=0, columnspan=2, sticky=tk.W); r += 1

        tk.Frame(parent, height=6).grid(row=r, column=0); r += 1

        # Location / output options
        self.v_all_locs = tk.BooleanVar(value=True)
        tk.Checkbutton(parent, text="Print All Locations?", variable=self.v_all_locs,
                       font=font).grid(row=r, column=0, columnspan=2, sticky=tk.W); r += 1

        loc_row = tk.Frame(parent)
        loc_row.grid(row=r, column=0, columnspan=2, sticky=tk.W); r += 1
        tk.Label(loc_row, text="Print Loc or Cust Name", font=font).pack(side=tk.LEFT, padx=(0, 4))
        self.v_loc_cname = tk.StringVar(value="C")
        tk.Entry(loc_row, textvariable=self.v_loc_cname, width=2, font=font).pack(side=tk.LEFT)
        tk.Label(loc_row, text="(C=Cust  L=Loc)", font=font_sm).pack(side=tk.LEFT, padx=4)

        tk.Frame(parent, height=4).grid(row=r, column=0); r += 1

        # Print Last Operation
        lastop_row = tk.Frame(parent)
        lastop_row.grid(row=r, column=0, columnspan=2, sticky=tk.W); r += 1
        tk.Label(lastop_row, text="Print Last Operation", font=font).pack(side=tk.LEFT, padx=(0, 4))
        self.v_last_op = tk.StringVar(value="N")
        tk.Entry(lastop_row, textvariable=self.v_last_op, width=2, font=font).pack(side=tk.LEFT)
        tk.Label(lastop_row, text="[C Q A S N]", font=font_sm).pack(side=tk.LEFT, padx=4)

        tk.Frame(parent, height=6).grid(row=r, column=0); r += 1

        # Boolean special filters
        self.v_orphans    = tk.BooleanVar(value=False)
        self.v_so_only    = tk.BooleanVar(value=False)
        self.v_unstarted  = tk.BooleanVar(value=False)
        tk.Checkbutton(parent, text="Print Only WOs without SOs?", variable=self.v_orphans,
                       font=font).grid(row=r, column=0, columnspan=2, sticky=tk.W); r += 1
        tk.Checkbutton(parent, text="Print Only WOs with SOs?", variable=self.v_so_only,
                       font=font).grid(row=r, column=0, columnspan=2, sticky=tk.W); r += 1
        tk.Checkbutton(parent, text="Print Only Unstarted WOs?", variable=self.v_unstarted,
                       font=font).grid(row=r, column=0, columnspan=2, sticky=tk.W); r += 1

    def _build_right(self, parent, font, font_bold):
        FONT_SM = ("Arial", 7)

        def srch_btn(parent, row_idx, fetcher, v_from, v_thru, title, filtered_fetcher=None):
            tk.Button(
                parent, text="...", width=2, font=FONT_SM,
                command=lambda f=fetcher, ff=filtered_fetcher: SearchDialog(
                    self, title, f, v_from, v_thru, ff)
            ).grid(row=row_idx, column=5, sticky=tk.W, padx=(2, 0))

        def row(parent, label, row_idx, v_from, v_thru, is_date=False, width=12,
                fetcher=None, title="", filtered_fetcher=None):
            tk.Label(parent, text=label, font=font).grid(row=row_idx, column=0, sticky=tk.E, padx=(0, 4), pady=2)
            tk.Label(parent, text="From", font=font).grid(row=row_idx, column=1, sticky=tk.W)
            w = 10 if is_date else width
            tk.Entry(parent, textvariable=v_from, width=w, font=font).grid(row=row_idx, column=2, sticky=tk.W, padx=(2, 4))
            tk.Label(parent, text="Thru", font=font).grid(row=row_idx, column=3, sticky=tk.W)
            tk.Entry(parent, textvariable=v_thru, width=w, font=font).grid(row=row_idx, column=4, sticky=tk.W, padx=2)
            if fetcher:
                srch_btn(parent, row_idx, fetcher, v_from, v_thru, title, filtered_fetcher)

        ri = 0
        D = "00/00/00"
        self.v_from_sstart = tk.StringVar(value=D); self.v_thru_sstart = tk.StringVar(value=D)
        self.v_from_sfin   = tk.StringVar(value=D); self.v_thru_sfin   = tk.StringVar(value=D)
        self.v_from_ddate  = tk.StringVar(value=D); self.v_thru_ddate  = tk.StringVar(value=D)
        self.v_from_wo     = tk.StringVar(); self.v_thru_wo     = tk.StringVar()
        self.v_from_job    = tk.StringVar(); self.v_thru_job    = tk.StringVar()
        self.v_from_item   = tk.StringVar(); self.v_thru_item   = tk.StringVar()
        self.v_from_cust   = tk.StringVar(); self.v_thru_cust   = tk.StringVar()
        self.v_from_cusord = tk.StringVar(); self.v_thru_cusord = tk.StringVar()
        self.v_from_class  = tk.StringVar(); self.v_thru_class  = tk.StringVar()
        self.v_from_plan   = tk.StringVar(); self.v_thru_plan   = tk.StringVar()
        self.v_from_so     = tk.StringVar(); self.v_thru_so     = tk.StringVar()
        self.v_note_type   = tk.StringVar()

        row(parent, "WO Start Date", ri, self.v_from_sstart, self.v_thru_sstart, is_date=True); ri += 1
        row(parent, "WO Fin Date",   ri, self.v_from_sfin,   self.v_thru_sfin,   is_date=True); ri += 1
        row(parent, "WO Due Date",   ri, self.v_from_ddate,  self.v_thru_ddate,  is_date=True); ri += 1
        row(parent, "WO Number",    ri, self.v_from_wo,  self.v_thru_wo,  width=10,
            fetcher=_fetch_wo,
            filtered_fetcher=lambda: _fetch_wo_filtered(self._collect_filters()),
            title="Search WO Number"); ri += 1
        row(parent, "Job Number",   ri, self.v_from_job, self.v_thru_job, width=10,
            fetcher=lambda: _fetch_distinct("WORKORD", "MTWO_WIP_PROJ"),
            title="Search Job Number"); ri += 1
        row(parent, "Item Number",  ri, self.v_from_item, self.v_thru_item, width=16,
            fetcher=_fetch_item,
            filtered_fetcher=lambda: _fetch_item_filtered(self._collect_filters()),
            title="Search Item Number"); ri += 1
        row(parent, "Customer",     ri, self.v_from_cust, self.v_thru_cust, width=10,
            fetcher=_fetch_cust,
            filtered_fetcher=lambda: _fetch_cust_filtered(self._collect_filters()),
            title="Search Customer"); ri += 1
        row(parent, "Cust PO",       ri, self.v_from_cusord, self.v_thru_cusord, width=16,
            fetcher=lambda: _fetch_distinct("WORKORD", "MTWO_WIP_CUSORD"),
            title="Search Cust PO"); ri += 1
        row(parent, "Item Class",    ri, self.v_from_class, self.v_thru_class, width=6,
            fetcher=lambda: _fetch_distinct("BKICMSTR", "BKIC_PROD_CLASS"),
            title="Search Item Class"); ri += 1
        row(parent, "Planner Code",  ri, self.v_from_plan, self.v_thru_plan, width=6,
            fetcher=lambda: _fetch_distinct("WORKORD", "MTWO_WIP_PROJ"),
            title="Search Planner Code"); ri += 1
        row(parent, "SO Number",     ri, self.v_from_so, self.v_thru_so, width=10,
            fetcher=lambda: _fetch_distinct("WORKORD", "MTWO_WIP_SONUM"),
            title="Search SO Number"); ri += 1

        tk.Label(parent, text="Dates: MM/DD/YYYY  (00/00/00 = no filter)", font=("Arial", 7),
                 fg="gray").grid(row=ri, column=0, columnspan=6, sticky=tk.W, pady=(4, 0))

    def _toggle_classes(self):
        state = tk.DISABLED if self.v_all_class.get() else tk.NORMAL
        for e in self._class_entries:
            e.config(state=state)

    # ---- Print action ----

    def _collect_filters(self):
        return {
            'sort_by':       self.v_sort.get(),
            'st_sched':      self.v_st_sched.get(),
            'st_firm':       self.v_st_firm.get(),
            'st_rel':        self.v_st_rel.get(),
            'st_closed':     self.v_st_closed.get(),
            'from_sstart':   self.v_from_sstart.get().strip(),
            'thru_sstart':   self.v_thru_sstart.get().strip(),
            'from_sfin':     self.v_from_sfin.get().strip(),
            'thru_sfin':     self.v_thru_sfin.get().strip(),
            'from_ddate':    self.v_from_ddate.get().strip(),
            'thru_ddate':    self.v_thru_ddate.get().strip(),
            'from_wo':       self.v_from_wo.get().strip(),
            'thru_wo':       self.v_thru_wo.get().strip(),
            'from_job':      self.v_from_job.get().strip(),
            'thru_job':      self.v_thru_job.get().strip(),
            'from_item':     self.v_from_item.get().strip(),
            'thru_item':     self.v_thru_item.get().strip(),
            'from_cust':     self.v_from_cust.get().strip(),
            'thru_cust':     self.v_thru_cust.get().strip(),
            'from_cusord':   self.v_from_cusord.get().strip(),
            'thru_cusord':   self.v_thru_cusord.get().strip(),
            'from_class':    self.v_from_class.get().strip(),
            'thru_class':    self.v_thru_class.get().strip(),
            'from_plan':     self.v_from_plan.get().strip(),
            'thru_plan':     self.v_thru_plan.get().strip(),
            'from_so':       self.v_from_so.get().strip(),
            'thru_so':       self.v_thru_so.get().strip(),
            'last_op_mode':  self.v_last_op.get().strip().upper(),
            'loc_cname':     self.v_loc_cname.get().strip().upper(),
            'so_only':       self.v_so_only.get(),
            'orphans_only':  self.v_orphans.get(),
            'unstarted_only':self.v_unstarted.get(),
            'all_class':     self.v_all_class.get(),
            'blank_class':   self.v_blank_class.get(),
            'class_codes':   [v.get().strip().upper() for v in self._class_vars],
        }

    def _on_print(self):
        filters = self._collect_filters()
        if not any([filters['st_sched'], filters['st_firm'], filters['st_rel'], filters['st_closed']]):
            messagebox.showwarning("No Status", "Select at least one status.")
            return

        self.config(cursor="watch")
        self.update()
        try:
            rows = build_and_run(filters)
        except Exception as ex:
            messagebox.showerror("Query Error", str(ex))
            self.config(cursor="")
            return

        if not rows:
            proceed = messagebox.askyesno(
                "No Results",
                "No work orders matched the selected filters.\n\nPrint an empty report (criteria page only)?",
                default="no"
            )
            if not proceed:
                self.config(cursor="")
                return

        out = os.path.join(tempfile.gettempdir(), "wo_schedule.pdf")
        try:
            generate_pdf(rows, filters, self.company_name, out)
        except Exception as ex:
            messagebox.showerror("Report Error", str(ex))
            self.config(cursor="")
            return

        self.config(cursor="")
        subprocess.Popen(["start", "", out], shell=True)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    # --- Startup connectivity check ---
    root = tk.Tk()
    root.withdraw()

    while True:
        try:
            pyodbc.connect(f"DSN={DSN}", autocommit=True, timeout=5).close()
            break
        except Exception as ex:
            err = str(ex)
            new_dsn = simpledialog.askstring(
                "Database Connection Failed",
                f"Could not connect using DSN=\"{DSN}\".\n\n"
                f"Error: {err}\n\n"
                "This program requires a Pervasive SQL ODBC data source.\n"
                "Check that the Pervasive ODBC driver is installed and a\n"
                "system DSN pointing to the EvoERP database exists.\n\n"
                "Enter a different DSN name to try, or cancel to exit:",
                initialvalue=DSN,
                parent=root,
            )
            if not new_dsn:
                root.destroy()
                sys.exit(0)
            DSN = new_dsn.strip()
            _save_dsn(DSN)

    root.destroy()
    app = WOScheduleApp()
    app.mainloop()
