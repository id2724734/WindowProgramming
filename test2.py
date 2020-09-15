import wx

class ChildFrame(wx.Frame):
    def __init__(self, parent, title=None, size=(200, 200)):
        super().__init__(parent, title=title, size=size)
        self.gui()

    def gui(self):
        # 메뉴 디자인 : 고정식 메뉴, 이동식 메뉴
        # MenuBar, Menu, MenuItem
        menubar = wx.MenuBar()
        mnuFile = wx.Menu()
        mnuEdit = wx.Menu()

        mnuFile_new = wx.MenuItem(mnuFile, wx.ID_NEW, "New", "New Document")
        mnuFile_open = wx.MenuItem(mnuFile, wx.ID_OPEN, "Open", "파일 열기")
        mnuFile_exit = wx.MenuItem(mnuFile, wx.ID_EXIT, "Exit", "프로그램 종료")

        mnuFile.Append(mnuFile_new)
        mnuFile.Append(mnuFile_open)
        mnuFile.AppendSeparator()
        mnuFile.Append(mnuFile_exit)
        menubar.Append(mnuFile, "파일")
        menubar.Append(mnuEdit, "편집")
        self.SetMenuBar(menubar)        #상단 메뉴바

        self.txtA = wx.TextCtrl(self, style=wx.TE_MULTILINE) #여러 줄로 텍스트 입력을 가능하게 함

        self.Bind(wx.EVT_MENU, self.onNew, mnuFile_new)
        self.Bind(wx.EVT_MENU, self.onOpen, mnuFile_open)
        self.Bind(wx.EVT_MENU, self.onExit, mnuFile_exit)

        # self.Move(100, 50)
        self.Center()
        self.Show(True)


    def onNew(self, ev):    #윈도우 프로그래밍 설계시 이벤트 처리 메서드 앞에 on을 붙이는 것이 관례
        self.txtA.SetLabelText("새 문서를 선택하였습니다.")

    def onOpen(self, ev):
        # self.txtA.SetLabelText("파일 열기를 선택하였습니다.")
        # f = open("C:\\Users\\id272\\LSJ\\git따라해.txt", "r", encoding = "utf-8")

        dlg = wx.FileDialog(self, "파일 선택", "c:\\", "", "*.*", style=wx.ID_OPEN)

        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()

        f = open(path, "r", encoding = "utf-8")
        data = f.read()
        self.txtA.SetLabelText(data)
        f.close()

    def onExit(self, ev):
        self.txtA.SetLabelText("프로그램 종료를 선택하였습니다.")
        self.Close(True) # 기본값이 False 이므로 True로 해준다

if __name__ == "__main__":
    app = wx.App()
    frame = ChildFrame(None, "간단한 메모장 프로그램", (400, 600))
    app.MainLoop()