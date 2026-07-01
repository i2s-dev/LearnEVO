object EditForm2: TEditForm2
  Left = 499
  Top = 225
  Width = 216
  Height = 119
  Hint = 'S:\tas70\wtaschkintcompany.dfm'
  BorderIcons = []
  Caption = 'Include which companies'
  Color = clBtnFace
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -13
  Font.Name = 'Arial'
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
  OldCreateOrder = False
  No_Refresh = False
  ScreenPos = tpDesktopCenter
  SpecifiedTop = 0
  SpecifiedLeft = 0
  RememberSizeDate = 39140.723155162040000000
  SourceAttached = False
  PixelsPerInch = 96
  TextHeight = 16
  object Panel1: TPanel
    Left = 0
    Top = 0
    Width = 208
    Height = 92
    Align = alClient
    BevelInner = bvRaised
    BevelOuter = bvNone
    BorderStyle = bsSingle
    TabOrder = 0
    object Button1: TButton
      Left = 119
      Top = 55
      Width = 75
      Height = 25
      Caption = '&OK'
      ModalResult = 1
      TabOrder = 2
    end
    object rdbCur: TTASRadioButton
      Left = 20
      Top = 7
      Width = 146
      Height = 17
      Caption = 'Current Company'
      Checked = True
      TabOrder = 0
      TabStop = True
      DispPrgLoc = -1
      ClickPrgLoc = -1
      ChangePrgLoc = 0
      PrePrgLoc = -1
      PostPrgLoc = -1
      ValidPrgLoc = -1
      Group = 0
      NoClickOn = False
      NoClickOff = False
      ReturnIsTab = False
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
    object rdbAll: TTASRadioButton
      Left = 20
      Top = 27
      Width = 154
      Height = 17
      Caption = 'All Companies'
      TabOrder = 1
      DispPrgLoc = -1
      ClickPrgLoc = -1
      ChangePrgLoc = 0
      PrePrgLoc = -1
      PostPrgLoc = -1
      ValidPrgLoc = -1
      Group = 0
      NoClickOn = False
      NoClickOff = False
      ReturnIsTab = False
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
  end
end
