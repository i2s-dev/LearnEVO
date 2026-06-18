object EditForm1: TEditForm1
  Left = 392
  Top = 111
  Width = 785
  Height = 592
  Hint = 'S:\tas70\WTASFLLKUP.DFM'
  Caption = 'File Lookup'
  Color = clBtnFace
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -11
  Font.Name = 'MS Sans Serif'
  Font.Style = []
  FormStyle = fsStayOnTop
  Icon.Data = {
    000001000100202010FF00000000E80200001600000028000000200000004000
    0000010004000000000000000000000000000000000000000000000000000000
    0000000080000080000000808000800000008000800080800000C0C0C0008080
    80000000FF0000FF000000FFFF00FF000000FF00FF00FFFF0000FFFFFF000000
    0000000000000000000000000000000000000000000000000000000000000000
    000000000FFFFFFFFF00000000000000000000FFFFFFFFFFFFFFF00000000000
    0000FFFFFFFFFFFFFFFFFF0000000000000FFFFFF00000000FFFFFFF00000000
    00FFFFF0000000000000FFFF000000000FFFF0000000000000000FFFF0000000
    0FFF000000000000000000FFFF000000FFFF000FFFF000FFFFF0000000000000
    FFF000FFFFFF0FFFFFFF00000000000FFFF00FFFFFFFFFFFFFFFFF000000000F
    FF00FFFFFFFFFFFFF00FFFF00000000FFF00FFFFF000FFFFF000FFF00000000F
    FF00FFFF00000FFFF0000FFF0000000FFF00FFFF00000FFFF0000FFF0000000F
    FF00FFFF000000FFFF0000FFF000000FFF00FFFF000000FFFF0000FFF000000F
    FF00FFFFF00000FFFF0000FFF0000000FFF00FFFF00000FFFF0000FFF0000000
    FFF00FFFFF000FFFFF0000FFF0000000FFF000FFFFFFFFFFFF0000FFF0000000
    0FFF00FFFFFFFFFFFFF00FFFF00000000FFFF00FFFFFFF0FFFF00FFF00000000
    00FFFF000FFFF00FFFF0FFFF00000000000FFFF000000000000FFFF000000000
    0000FFFFF00000000FFFFF000000000000000FFFFFFFFFFFFFFFF00000000000
    000000FFFFFFFFFFFFFF000000000000000000000FFFFFFFF000000000000000
    0000000000000000000000000000000000000000000000000000000000000000
    0000000000000000000000000000000000000000000000000000000000000000
    0000000000000000000000000000000000000000000000000000000000000000
    0000000000000000000000000000000000000000000000000000000000000000
    000000000000000000000000000000000000000000000000000000000000}
  OldCreateOrder = True
  No_Refresh = False
  OnStart = 'fllkupStart'
  ScreenPos = tpDesktopCenter
  SpecifiedTop = 0
  SpecifiedLeft = 0
  RememberSizeDate = 38212.815758240740000000
  SourceAttached = False
  DesignSize = (
    777
    565)
  PixelsPerInch = 96
  TextHeight = 13
  object fsFileLocLU: TTASENTER
    Left = 12
    Top = 0
    Width = 121
    Height = 21
    CharCase = ecUpperCase
    TabOrder = 0
    DispPrgLoc = -1
    ClickPrgLoc = -1
    ChangePrgLoc = 0
    PrePrgLoc = -1
    PostPrgLoc = -1
    ValidPrgLoc = -1
    ValidCheckOnExit = False
    ValidUserEsc = False
    ValidExprLoc = 0
    ValidExprTyp = #0
    Group = 0
    NoClickOn = False
    NoClickOff = False
    ReturnIsTab = True
    SelectStart = 0
    PreRetFalse = False
    EntryFont.Charset = DEFAULT_CHARSET
    EntryFont.Color = clWindowText
    EntryFont.Height = -11
    EntryFont.Name = 'MS Sans Serif'
    EntryFont.Style = []
    EntryBGColor = clWhite
    EntryUseDflt = True
    FldModified = False
  end
  object dgFileLocLU: TTASDataGrid
    Left = 12
    Top = 24
    Width = 741
    Height = 487
    Anchors = [akLeft, akTop, akRight, akBottom]
    ColCount = 4
    Options = [goFixedVertLine, goFixedHorzLine, goVertLine, goHorzLine, goDrawFocusSelected, goRowSelect]
    TabOrder = 1
    UpCase = True
    StartAtEnd = False
    PrePrgLoc = 0
    PostPrgLoc = 0
    Navigation.AllowInsertRow = False
    Navigation.AllowDeleteRow = False
    Navigation.AdvanceOnEnter = True
    Navigation.AdvanceAtEnd = False
    Navigation.AdvanceDirection = adLeftRight
    Navigation.AdvanceAuto = False
    Navigation.InsertPosition = pInsertBefore
    Navigation.CursorWalkEditor = False
    Navigation.AllowAddRecListF = False
    MouseActions.ColSelect = False
    MouseActions.RowSelect = False
    MouseActions.DirectEdit = False
    MouseActions.DirectComboDrop = False
    MouseActions.CaretPositioning = False
    PasswordChar = '*'
    Columns = <
      item
        Color = clWindow
        Width = 159
        Alignment = taLeftJustify
        Header = 'File Name'
        Font.Charset = DEFAULT_CHARSET
        Font.Color = clWindowText
        Font.Height = -11
        Font.Name = 'MS Sans Serif'
        Font.Style = []
        Editor = edDefault
        Fixed = False
        ReadOnly = False
        Password = False
        ComboItemsSort = False
        SpinMin = 0
        SpinMax = 0
        SpinStep = 0
        EditLength = 0
        Borders = []
        BorderPen.Color = clSilver
        FieldName = 'LOC_FILE_NAME  '
        CharCase = ecNormal
        Name = 'gcFileName'
        PrePrgLoc = 0
        PostPrgLoc = 0
        ValidPrgLoc = 0
        ClickPrgLoc = 0
        ChangePrgLoc = 0
        DecimalChrs = 2
        FormatOnEnter = True
        ValidCheckOnExit = False
        ValidUserEsc = False
        ValidExprLoc = 0
        ValidExprTyp = #0
        TimeFieldType = tf_5
        ElapsedTime = False
      end
      item
        Color = clWindow
        Width = 50
        Alignment = taLeftJustify
        Header = 'Ext'
        Font.Charset = DEFAULT_CHARSET
        Font.Color = clWindowText
        Font.Height = -11
        Font.Name = 'MS Sans Serif'
        Font.Style = []
        Editor = edDefault
        Fixed = False
        ReadOnly = False
        Password = False
        ComboItemsSort = False
        SpinMin = 0
        SpinMax = 0
        SpinStep = 0
        EditLength = 0
        Borders = []
        BorderPen.Color = clSilver
        FieldName = 'LOC_COMP_CODE  '
        CharCase = ecNormal
        Name = 'gcExtenstion'
        PrePrgLoc = 0
        PostPrgLoc = 0
        ValidPrgLoc = 0
        ClickPrgLoc = 0
        ChangePrgLoc = 0
        DecimalChrs = 2
        FormatOnEnter = True
        ValidCheckOnExit = False
        ValidUserEsc = False
        ValidExprLoc = 0
        ValidExprTyp = #0
        TimeFieldType = tf_5
        ElapsedTime = False
      end
      item
        Color = clWindow
        Width = 90
        Alignment = taLeftJustify
        Header = 'FD Name'
        Font.Charset = DEFAULT_CHARSET
        Font.Color = clWindowText
        Font.Height = -11
        Font.Name = 'MS Sans Serif'
        Font.Style = []
        Editor = edDefault
        Fixed = False
        ReadOnly = False
        Password = False
        ComboItemsSort = False
        SpinMin = 0
        SpinMax = 0
        SpinStep = 0
        EditLength = 0
        Borders = []
        BorderPen.Color = clSilver
        FieldName = 'LOC_BUFF_NAME  '
        CharCase = ecNormal
        Name = 'gcBuffName'
        PrePrgLoc = 0
        PostPrgLoc = 0
        ValidPrgLoc = 0
        ClickPrgLoc = 0
        ChangePrgLoc = 0
        DecimalChrs = 2
        FormatOnEnter = True
        ValidCheckOnExit = False
        ValidUserEsc = False
        ValidExprLoc = 0
        ValidExprTyp = #0
        TimeFieldType = tf_5
        ElapsedTime = False
      end
      item
        Color = clWindow
        Width = 421
        Alignment = taLeftJustify
        Header = 'Path'
        Font.Charset = DEFAULT_CHARSET
        Font.Color = clWindowText
        Font.Height = -11
        Font.Name = 'MS Sans Serif'
        Font.Style = []
        Editor = edDefault
        Fixed = False
        ReadOnly = False
        Password = False
        ComboItemsSort = False
        SpinMin = 0
        SpinMax = 0
        SpinStep = 0
        EditLength = 0
        Borders = []
        BorderPen.Color = clSilver
        FieldName = 'LOC_LOCATION   '
        CharCase = ecNormal
        Name = 'gcPath'
        PrePrgLoc = 0
        PostPrgLoc = 0
        ValidPrgLoc = 0
        ClickPrgLoc = 0
        ChangePrgLoc = 0
        DecimalChrs = 2
        FormatOnEnter = True
        ValidCheckOnExit = False
        ValidUserEsc = False
        ValidExprLoc = 0
        ValidExprTyp = #0
        TimeFieldType = tf_5
        ElapsedTime = False
      end>
    ExtraFields = <>
    AutoNumAlign = False
    SelectionColor = clHighlight
    SelectionTextColor = clHighlightText
    SelectionRectangle = False
    FixedFont.Charset = DEFAULT_CHARSET
    FixedFont.Color = clWindowText
    FixedFont.Height = -11
    FixedFont.Name = 'MS Sans Serif'
    FixedFont.Style = []
    VAlignment = vtaTop
    Hovering = False
    EnhRowColMove = False
    HintColor = clYellow
    FastSearchFld = 'fsFileLocLU'
    CurrentRow = 1
    CurrentCol = 1
    GridFileHandle = 0
    GridFileKeyNum = 0
    NoAutoUpdate = False
    ColWidths = (
      159
      50
      90
      421)
  end
  object btnSelect: TButton
    Left = 14
    Top = 515
    Width = 75
    Height = 25
    Caption = 'S&elect'
    Font.Charset = DEFAULT_CHARSET
    Font.Color = clWindowText
    Font.Height = -13
    Font.Name = 'MS Sans Serif'
    Font.Style = []
    ModalResult = 1
    ParentFont = False
    TabOrder = 2
  end
  object btnCancel: TButton
    Left = 678
    Top = 515
    Width = 75
    Height = 25
    Cancel = True
    Caption = 'C&ancel'
    Font.Charset = DEFAULT_CHARSET
    Font.Color = clWindowText
    Font.Height = -13
    Font.Name = 'MS Sans Serif'
    Font.Style = []
    ModalResult = 2
    ParentFont = False
    TabOrder = 3
  end
  object StatusBar1: TStatusBar
    Left = 0
    Top = 546
    Width = 777
    Height = 19
    Panels = <>
  end
end
