# Hello World mit Eingabefeld und MessageBox

import wx

from generated import AbstractMainPanel


class MainPanel(AbstractMainPanel):
    def on_button_click(self, event):
        self.show_messagebox()

    def on_text_enter(self, event):
        self.show_messagebox()

    def show_messagebox(self):
        name = self.name_input.Value
        message = "Hello {}!".format(name)
        caption = "Your greeting"
        dlg = wx.MessageDialog(self, message, caption, wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()

app = wx.App()
frm = wx.Frame(None, title="Hello World")
pnl = MainPanel(frm)
frm.Show()
app.MainLoop()
