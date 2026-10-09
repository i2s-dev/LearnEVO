#!/usr/bin/env python3
"""EVO Menu Access Browser — By User / By Form"""

import os
import struct
import tempfile
import tkinter as tk
from tkinter import messagebox, filedialog
from datetime import datetime

import win32print
import win32api

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.enums import TA_LEFT, TA_CENTER

DBF_PATH = r"C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\samples\BKMENUSU.DBF"
DBT_PATH = r"C:\Users\tsinclair.I2SYSTEMS\Documents\Visual Studio Code Projects\LearnEVO\samples\BKMENUSU.dbt"
BLOCK_SIZE = 512
DEFAULT_TEMPLATE = "USER"

# ── parser ────────────────────────────────────────────────────────────────────

def parse_bkmenusu():
    with open(DBF_PATH, 'rb') as f:
        raw = f.read()
    with open(DBT_PATH, 'rb') as f:
        dbt = f.read()

    header_size = struct.unpack_from('<H', raw, 8)[0]
    rec_size    = struct.unpack_from('<H', raw, 10)[0]
    n_records   = struct.unpack_from('<I', raw, 4)[0]

    fields, off = [], 32
    while raw[off] != 0x0D:
        name  = raw[off:off+11].rstrip(b'\x00').decode('ascii', errors='replace')
        ftype = chr(raw[off+11])
        flen  = raw[off+16]
        fields.append((name, ftype, flen))
        off += 32

    fo, cum = {}, 1
    for name, ftype, flen in fields:
        fo[name] = (cum, ftype, flen)
        cum += flen

    mnu_ac_o, _, mnu_ac_l = fo['MNU_AC']
    mnu_su_o, _, mnu_su_l = fo['MNU_SU']

    def read_memo(block_num):
        if block_num <= 0:
            return b''
        start = block_num * BLOCK_SIZE
        if start >= len(dbt):
            return b''
        end = dbt.find(b'\x1a\x1a', start)
        return dbt[start:end if end != -1 else start + 65536]

    def parse_items(memo_bytes):
        items = []
        for line in memo_bytes.decode('ascii', errors='replace').splitlines():
            parts = [p.strip('"') for p in line.split('","')]
            if len(parts) >= 8:
                code = parts[6].strip()
                desc = parts[7].strip()
                if code:
                    items.append((code, desc))
        return items

    user_items, code_desc = {}, {}
    for i in range(n_records):
        rs = header_size + i * rec_size
        if raw[rs:rs+1] == b'*':
            continue
        mnu_ac = raw[rs + mnu_ac_o : rs + mnu_ac_o + mnu_ac_l].decode('ascii', errors='replace').strip()
        ptr    = raw[rs + mnu_su_o : rs + mnu_su_o + mnu_su_l].decode('ascii', errors='replace').strip()
        try:
            block = int(ptr) if ptr else 0
        except ValueError:
            block = 0
        items = parse_items(read_memo(block))
        seen = set()
        items = [(c, d) for c, d in items if not (c in seen or seen.add(c))]
        user_items[mnu_ac] = items
        for code, desc in items:
            code_desc.setdefault(code, desc)

    return user_items, code_desc


# ── PDF report builder ────────────────────────────────────────────────────────

CLR_GREEN_DARK  = colors.HexColor('#1b5e20')
CLR_GREEN_LIGHT = colors.HexColor('#dff0d8')
CLR_BLUE_DARK   = colors.HexColor('#0d47a1')
CLR_BLUE_LIGHT  = colors.HexColor('#e3f2fd')
CLR_HEADER_BG   = colors.HexColor('#2c3e50')
CLR_GREY        = colors.HexColor('#e0e0e0')


def build_pdf(path, mode, chosen, user_items, code_desc, code_users, default_codes):
    doc = SimpleDocTemplate(
        path,
        pagesize=letter,
        leftMargin=0.75*inch, rightMargin=0.75*inch,
        topMargin=0.75*inch,  bottomMargin=0.75*inch,
    )
    styles = getSampleStyleSheet()
    normal = styles['Normal']

    title_style = ParagraphStyle('title', fontName='Helvetica-Bold', fontSize=16,
                                 textColor=colors.white, alignment=TA_LEFT)
    h1_style    = ParagraphStyle('h1',    fontName='Helvetica-Bold', fontSize=11,
                                 textColor=colors.white, alignment=TA_LEFT)
    body_style  = ParagraphStyle('body',  fontName='Helvetica',      fontSize=9,
                                 leading=13)
    small_style = ParagraphStyle('small', fontName='Helvetica',      fontSize=8,
                                 textColor=colors.grey, leading=11)

    story = []
    ts = datetime.now().strftime('%B %d, %Y  %I:%M %p')

    # ── title block ──
    title_text = f'EVO Menu Access Report'
    sub_text   = f'Generated: {ts}'
    story.append(Table(
        [[Paragraph(title_text, title_style)],
         [Paragraph(sub_text,   ParagraphStyle('sub', fontName='Helvetica', fontSize=9,
                                               textColor=colors.lightgrey))]],
        colWidths=[7*inch],
        style=TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), CLR_HEADER_BG),
            ('TOPPADDING',    (0,0), (-1,-1), 8),
            ('BOTTOMPADDING', (0,0), (-1,-1), 8),
            ('LEFTPADDING',   (0,0), (-1,-1), 12),
        ])
    ))
    story.append(Spacer(1, 0.2*inch))

    if mode == 'user':
        _build_user_section(story, chosen, user_items, default_codes,
                            h1_style, body_style, small_style)
    else:
        _build_form_section(story, chosen, code_desc, code_users, default_codes,
                            h1_style, body_style, small_style)

    doc.build(story)


def _section_header(text, bg_color, text_color=colors.white):
    return Table(
        [[Paragraph(text, ParagraphStyle('sh', fontName='Helvetica-Bold', fontSize=9,
                                         textColor=text_color))]],
        colWidths=[7*inch],
        style=TableStyle([
            ('BACKGROUND',    (0,0), (-1,-1), bg_color),
            ('TOPPADDING',    (0,0), (-1,-1), 4),
            ('BOTTOMPADDING', (0,0), (-1,-1), 4),
            ('LEFTPADDING',   (0,0), (-1,-1), 8),
        ])
    )


def _item_table(rows, row_bg, col_widths=(1.4*inch, 5.6*inch)):
    body_style = ParagraphStyle('bt', fontName='Courier', fontSize=8, leading=11)
    data = [[Paragraph(c, body_style), Paragraph(d, body_style)] for c, d in rows]
    ts = TableStyle([
        ('BACKGROUND',    (0,0), (-1,-1), row_bg),
        ('TOPPADDING',    (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('LEFTPADDING',   (0,0), (-1,-1), 16),
        ('GRID',          (0,0), (-1,-1), 0.25, colors.HexColor('#cccccc')),
    ])
    return Table(data, colWidths=list(col_widths), style=ts, repeatRows=0)


def _build_user_section(story, user, user_items, default_codes, h1, body, small):
    items = user_items.get(user, [])
    default_items = sorted([(c,d) for c,d in items if c in default_codes])
    extra_items   = sorted([(c,d) for c,d in items if c not in default_codes])

    # Subject header
    story.append(_section_header(
        f'User: {user}   |   {len(items)} total forms   '
        f'({len(default_items)} default + {len(extra_items)} additional)',
        CLR_HEADER_BG))
    story.append(Spacer(1, 0.1*inch))

    # Default access
    if default_items:
        story.append(_section_header(
            f'DEFAULT ACCESS — {len(default_items)} forms  '
            f'(inherited by all standard users)',
            CLR_GREEN_DARK))
        story.append(_item_table(default_items, CLR_GREEN_LIGHT))
        story.append(Spacer(1, 0.12*inch))

    # Additional access
    if extra_items:
        story.append(_section_header(
            f'ADDITIONAL ACCESS — {len(extra_items)} forms  '
            f'(above the USER template)',
            CLR_BLUE_DARK))
        story.append(_item_table(extra_items, CLR_BLUE_LIGHT))
        story.append(Spacer(1, 0.12*inch))

    if not items:
        story.append(Paragraph(
            'No explicit menu record found. This user inherits the USER template.',
            small))

    story.append(Paragraph(
        'Note: Users without an explicit BKMENUSU record inherit the USER template (DEFAULT items above).',
        small))


def _build_form_section(story, code, code_desc, code_users, default_codes, h1, body, small):
    desc      = code_desc.get(code, '')
    users     = sorted(code_users.get(code, []))
    is_default = code in default_codes

    story.append(_section_header(
        f'Form: {code}   |   {desc}   |   {len(users)} users with explicit access',
        CLR_HEADER_BG))
    story.append(Spacer(1, 0.1*inch))

    if is_default:
        story.append(_section_header(
            'DEFAULT FORM — part of the USER template. '
            'All standard users have this access by default.',
            CLR_GREEN_DARK))
        story.append(Spacer(1, 0.08*inch))

    story.append(_section_header(
        f'Users with explicit {code} access ({len(users)})',
        colors.HexColor('#546e7a'), text_color=colors.white))

    if users:
        # Single-column user list, two columns side-by-side
        mid   = (len(users) + 1) // 2
        left  = users[:mid]
        right = users[mid:]
        body_s = ParagraphStyle('ul', fontName='Courier', fontSize=9, leading=13)
        rows = []
        for i in range(mid):
            ltext = left[i]  if i < len(left)  else ''
            rtext = right[i] if i < len(right) else ''
            rows.append([Paragraph(ltext, body_s), Paragraph(rtext, body_s)])
        t = Table(rows, colWidths=[3.5*inch, 3.5*inch],
                  style=TableStyle([
                      ('BACKGROUND',    (0,0), (-1,-1),
                       CLR_GREEN_LIGHT if is_default else colors.HexColor('#f5f5f5')),
                      ('TOPPADDING',    (0,0), (-1,-1), 2),
                      ('BOTTOMPADDING', (0,0), (-1,-1), 2),
                      ('LEFTPADDING',   (0,0), (-1,-1), 12),
                      ('GRID',          (0,0), (-1,-1), 0.25, colors.HexColor('#cccccc')),
                  ]))
        story.append(t)
    else:
        story.append(Paragraph('No users have this form in their explicit record.', small))

    story.append(Spacer(1, 0.1*inch))
    if is_default:
        story.append(Paragraph(
            'Note: This is a DEFAULT form. In addition to the users listed above, '
            'any user without an explicit BKMENUSU record also has this access.',
            small))


# ── print dialog ──────────────────────────────────────────────────────────────

class PrintDialog(tk.Toplevel):
    def __init__(self, parent, on_print):
        super().__init__(parent)
        self.title("Print Report")
        self.resizable(False, False)
        self.grab_set()
        self.on_print = on_print

        tk.Label(self, text="Select Printer:", font=('Segoe UI', 10, 'bold'),
                 pady=8).pack(anchor='w', padx=16)

        # Printer list
        lf = tk.Frame(self)
        lf.pack(fill='both', expand=True, padx=16)
        self.printer_list = tk.Listbox(lf, font=('Segoe UI', 10), height=12,
                                       selectmode='single', exportselection=False,
                                       width=52)
        sb = tk.Scrollbar(lf, command=self.printer_list.yview)
        self.printer_list.config(yscrollcommand=sb.set)
        self.printer_list.pack(side='left', fill='both', expand=True)
        sb.pack(side='right', fill='y')

        self._printers = []
        default_printer = win32print.GetDefaultPrinter()
        printers = [p[2] for p in win32print.EnumPrinters(
            win32print.PRINTER_ENUM_LOCAL | win32print.PRINTER_ENUM_CONNECTIONS)]
        printers.sort(key=lambda p: (p != default_printer, p))

        for i, p in enumerate(printers):
            label = f'{"★ " if p == default_printer else "  "}{p}'
            self.printer_list.insert('end', label)
            self._printers.append(p)
            if p == default_printer:
                self.printer_list.selection_set(i)
                self.printer_list.see(i)

        btn_frame = tk.Frame(self, pady=10)
        btn_frame.pack(fill='x', padx=16)
        tk.Button(btn_frame, text="Print", font=('Segoe UI', 10), width=10,
                  bg='#2c3e50', fg='white', activebackground='#34495e',
                  command=self._do_print).pack(side='right', padx=4)
        tk.Button(btn_frame, text="Cancel", font=('Segoe UI', 10), width=10,
                  command=self.destroy).pack(side='right', padx=4)

        self.update_idletasks()
        pw, ph = self.winfo_reqwidth(), self.winfo_reqheight()
        x = parent.winfo_x() + (parent.winfo_width()  - pw) // 2
        y = parent.winfo_y() + (parent.winfo_height() - ph) // 2
        self.geometry(f'+{x}+{y}')

    def _do_print(self):
        sel = self.printer_list.curselection()
        if not sel:
            messagebox.showwarning("No Printer", "Please select a printer.", parent=self)
            return
        printer = self._printers[sel[0]]
        self.destroy()
        self.on_print(printer)


# ── main app ──────────────────────────────────────────────────────────────────

class App(tk.Tk):
    CLR_DEFAULT = '#dff0d8'
    CLR_CUSTOM  = '#ffffff'

    def __init__(self):
        super().__init__()
        self.title("EVO Menu Access")
        self.geometry("980x660")
        self.resizable(True, True)

        self.user_items, self.code_desc = parse_bkmenusu()
        self.default_codes = {c for c, _ in self.user_items.get(DEFAULT_TEMPLATE, [])}

        self.code_users = {}
        for user, items in self.user_items.items():
            for code, _ in items:
                self.code_users.setdefault(code, set()).add(user)
        self.code_users = {c: sorted(s) for c, s in self.code_users.items()}

        self._current_chosen = None
        self._build_ui()
        self._populate_left()

    # ── layout ────────────────────────────────────────────────────────────────

    def _build_ui(self):
        bar = tk.Frame(self, bg='#2c3e50', pady=6)
        bar.pack(fill='x')
        tk.Label(bar, text="EVO Menu Access", bg='#2c3e50', fg='white',
                 font=('Segoe UI', 13, 'bold')).pack(side='left', padx=16)

        self.mode = tk.StringVar(value='user')
        for val, txt in (('user', 'By User'), ('form', 'By Form')):
            tk.Radiobutton(bar, text=txt, variable=self.mode, value=val,
                           command=self._on_mode_change,
                           bg='#2c3e50', fg='white', selectcolor='#2c3e50',
                           activebackground='#2c3e50', activeforeground='white',
                           font=('Segoe UI', 11)).pack(side='left', padx=10)

        # Toolbar buttons
        tk.Button(bar, text='🖨  Print Report', font=('Segoe UI', 10),
                  bg='#e74c3c', fg='white', activebackground='#c0392b',
                  relief='flat', padx=10, pady=2,
                  command=self._on_save_pdf).pack(side='right', padx=4)
        tk.Button(bar, text='🖨  Send to Printer', font=('Segoe UI', 10),
                  bg='#555', fg='white', activebackground='#333',
                  relief='flat', padx=10, pady=2,
                  command=self._on_print).pack(side='right', padx=4)

        # Legend
        leg = tk.Frame(self, bg='#f8f8f8', pady=3)
        leg.pack(fill='x')
        tk.Label(leg, text="  ■ ", bg=self.CLR_DEFAULT, fg='#3a7d44').pack(side='left')
        tk.Label(leg, text="Default (USER template access)", bg='#f8f8f8',
                 font=('Segoe UI', 9)).pack(side='left')
        tk.Label(leg, text="   ■ ", bg='#ffffff', fg='#666').pack(side='left')
        tk.Label(leg, text="Additional / custom access", bg='#f8f8f8',
                 font=('Segoe UI', 9)).pack(side='left')

        pane = tk.PanedWindow(self, orient='horizontal', sashwidth=5, bg='#cccccc')
        pane.pack(fill='both', expand=True)

        # Left panel
        left = tk.Frame(pane, bg='#f0f0f0')
        pane.add(left, minsize=220)

        self.left_label = tk.Label(left, text='Select User:', bg='#f0f0f0',
                                   font=('Segoe UI', 10, 'bold'))
        self.left_label.pack(anchor='w', padx=6, pady=(6,2))

        self.search_var = tk.StringVar()
        self.search_var.trace('w', self._on_search)
        tk.Entry(left, textvariable=self.search_var, font=('Segoe UI', 10)
                 ).pack(fill='x', padx=6, pady=2)

        lf = tk.Frame(left)
        lf.pack(fill='both', expand=True, padx=6, pady=4)
        self.left_list = tk.Listbox(lf, font=('Consolas', 10), activestyle='dotbox',
                                    selectmode='single', exportselection=False)
        sb = tk.Scrollbar(lf, command=self.left_list.yview)
        self.left_list.config(yscrollcommand=sb.set)
        self.left_list.pack(side='left', fill='both', expand=True)
        sb.pack(side='right', fill='y')
        self.left_list.bind('<<ListboxSelect>>', self._on_select)

        self.count_label = tk.Label(left, text='', bg='#f0f0f0', font=('Segoe UI', 9),
                                    fg='#555')
        self.count_label.pack(anchor='w', padx=6, pady=(0,4))

        # Right panel
        right = tk.Frame(pane)
        pane.add(right, minsize=500)

        self.right_label = tk.Label(right, text='', font=('Segoe UI', 10, 'bold'),
                                    anchor='w')
        self.right_label.pack(fill='x', padx=8, pady=(6,2))

        rf = tk.Frame(right)
        rf.pack(fill='both', expand=True, padx=8, pady=4)
        self.right_list = tk.Listbox(rf, font=('Consolas', 10), activestyle='dotbox',
                                     selectmode='single', exportselection=False)
        sb2 = tk.Scrollbar(rf, command=self.right_list.yview)
        self.right_list.config(yscrollcommand=sb2.set)
        self.right_list.pack(side='left', fill='both', expand=True)
        sb2.pack(side='right', fill='y')

        self.status = tk.Label(self, text='', anchor='w', font=('Segoe UI', 9),
                               fg='#555', bd=1, relief='sunken')
        self.status.pack(fill='x', side='bottom')

    # ── left list ─────────────────────────────────────────────────────────────

    def _populate_left(self):
        query = self.search_var.get().strip().upper()
        self.left_list.delete(0, 'end')
        all_items = sorted(self.user_items.keys() if self.mode.get() == 'user'
                           else self.code_desc.keys())
        self.left_label.config(text='Select User:' if self.mode.get() == 'user'
                               else 'Select Form:')
        self._left_items = [x for x in all_items if query in x.upper()]
        for item in self._left_items:
            self.left_list.insert('end', item)
        self.count_label.config(text=f'{len(self._left_items)} shown')

    # ── right panel ───────────────────────────────────────────────────────────

    def _on_select(self, _=None):
        sel = self.left_list.curselection()
        if not sel:
            return
        self._current_chosen = self._left_items[sel[0]]
        self.right_list.delete(0, 'end')
        if self.mode.get() == 'user':
            self._show_user(self._current_chosen)
        else:
            self._show_form(self._current_chosen)

    def _show_user(self, user):
        items = self.user_items.get(user, [])
        default_items = sorted([(c,d) for c,d in items if c in self.default_codes])
        extra_items   = sorted([(c,d) for c,d in items if c not in self.default_codes])

        self.right_label.config(
            text=f'{user}   —   {len(items)} forms  '
                 f'({len(default_items)} default + {len(extra_items)} extra)')

        if default_items:
            self.right_list.insert('end', f'── DEFAULT ACCESS ({len(default_items)} items) ──────────────')
            self.right_list.itemconfig('end', bg='#c8e6c9', fg='#1b5e20')
            for c, d in default_items:
                self.right_list.insert('end', f'  {c:<12} {d}')
                self.right_list.itemconfig('end', bg=self.CLR_DEFAULT)

        if extra_items:
            self.right_list.insert('end', f'── ADDITIONAL ACCESS ({len(extra_items)} items) ───────────')
            self.right_list.itemconfig('end', bg='#bbdefb', fg='#0d47a1')
            for c, d in extra_items:
                self.right_list.insert('end', f'  {c:<12} {d}')

        if not items:
            self.right_list.insert('end', '  (no explicit menu items — inherits USER template)')

        self.status.config(text=f'Tip: Users not in BKMENUSU inherit the USER template '
                                f'({len(self.default_codes)} default items)')

    def _show_form(self, code):
        desc      = self.code_desc.get(code, '')
        users     = self.code_users.get(code, [])
        is_default = code in self.default_codes

        self.right_label.config(
            text=f'{code}  —  {desc}  —  {len(users)} users'
                 + ('  [DEFAULT]' if is_default else ''))

        if is_default:
            self.right_list.insert('end', '── DEFAULT form — part of USER template ──────────────')
            self.right_list.itemconfig('end', bg='#c8e6c9', fg='#1b5e20')
            self.right_list.insert('end', '   All standard users have this access by default.')
            self.right_list.itemconfig('end', bg=self.CLR_DEFAULT)
            self.right_list.insert('end', '')

        self.right_list.insert('end', f'── Users with explicit {code} access ({len(users)}) ──')
        self.right_list.itemconfig('end', bg='#e0e0e0', fg='#333')
        for u in users:
            self.right_list.insert('end', f'  {u}')
            if is_default:
                self.right_list.itemconfig('end', bg=self.CLR_DEFAULT)

        self.status.config(text='DEFAULT form — all standard users have this access.'
                           if is_default else 'Non-default — only listed users have access.')

    # ── print ─────────────────────────────────────────────────────────────────

    def _auto_name(self):
        date_str = datetime.now().strftime('%Y-%m-%d')
        label    = self._current_chosen.replace(' ', '_')
        mode_tag = 'User' if self.mode.get() == 'user' else 'Form'
        return f'EVO-{mode_tag}-{label}-{date_str}.pdf'

    def _on_save_pdf(self):
        if not self._current_chosen:
            messagebox.showinfo("Nothing Selected",
                                "Please select a user or form first.", parent=self)
            return
        out_path = filedialog.asksaveasfilename(
            parent=self,
            title='Save PDF Report',
            initialfile=self._auto_name(),
            defaultextension='.pdf',
            filetypes=[('PDF files', '*.pdf'), ('All files', '*.*')],
        )
        if not out_path:
            return
        try:
            build_pdf(out_path, self.mode.get(), self._current_chosen,
                      self.user_items, self.code_desc, self.code_users,
                      self.default_codes)
            os.startfile(out_path)
            self.status.config(text=f'Saved: {os.path.basename(out_path)}')
        except Exception as e:
            messagebox.showerror('Save Error', str(e), parent=self)

    def _on_print(self):
        if not self._current_chosen:
            messagebox.showinfo("Nothing Selected",
                                "Please select a user or form first.", parent=self)
            return
        PrintDialog(self, self._do_print)

    def _do_print(self, printer_name):
        tmp = tempfile.NamedTemporaryFile(suffix='.pdf', delete=False,
                                         prefix='evo-access-')
        tmp.close()
        try:
            build_pdf(tmp.name, self.mode.get(), self._current_chosen,
                      self.user_items, self.code_desc, self.code_users,
                      self.default_codes)
            win32api.ShellExecute(0, 'printto', tmp.name,
                                  f'"{printer_name}"', '.', 0)
            self.status.config(text=f'Sent to {printer_name}')
        except Exception as e:
            messagebox.showerror('Print Error', str(e), parent=self)

    # ── events ────────────────────────────────────────────────────────────────

    def _on_mode_change(self):
        self._current_chosen = None
        self.search_var.set('')
        self.right_list.delete(0, 'end')
        self.right_label.config(text='')
        self.status.config(text='')
        self._populate_left()

    def _on_search(self, *_):
        self._populate_left()


if __name__ == '__main__':
    App().mainloop()
