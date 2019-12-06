#
# Übung zum ListCtrl in wx / Einführung in die Dokumentation

import wx

from generated import AbstractMainPanel

class ListPanel(AbstractMainPanel):
    def on_input_text_enter(self, event):
        self.on_button_add(event)

    def on_button_add(self, event):
        self.main_list.Append([self.input_text.Value])
        self.input_text.Clear()
        self.input_text.SetFocus()

    def on_button_delete(self, event):
        def del_sel_items(item=self.main_list.GetFirstSelected()):
            if item != -1:
                del_sel_items(self.main_list.GetNextSelected(item))
                self.main_list.DeleteItem(item)
        del_sel_items()
        self.Refresh()

    def on_button_quit(self, event):
        self.Parent.Close() # close Frame

app = wx.App()
frm = wx.Frame(None, title="Item List")
pnl = ListPanel(frm)
frm.Show()
app.MainLoop()
