import wx
from generated import MyPanel1, MyPanel2

class MyPanel1Impl(MyPanel1):
    def on_click_one_to_two(self, event):
        frm = self.GetParent()
        self.Hide()
        pnl = MyPanel2Impl(frm)

class MyPanel2Impl(MyPanel2):
    def on_click_two_to_one(self, event):
        frm = self.GetParent()
        self.Hide()
        pnl = MyPanel1Impl(frm)

app = wx.App()
frm = wx.Frame(None, title="Panel Exchange Demo")
pnl = MyPanel1Impl(frm)
frm.Show()
app.MainLoop()
