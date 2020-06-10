# from https://www.blog.pythonlibrary.org/2017/09/28/wxpython-all-about-accelerators/ (modified)
import wx

class MyForm(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, title="Accelerator Tutorial",
                          size=(500,500))

        # Add a panel so it looks the correct on all platforms
        panel = wx.Panel(self, wx.ID_ANY)

        randomId = wx.Window.NewControlId()
        self.Bind(wx.EVT_MENU, self.onKeyCombo, id=randomId)
        accel_tbl = wx.AcceleratorTable([(wx.ACCEL_CTRL,  ord('Q'),
                                          randomId )])
        self.SetAcceleratorTable(accel_tbl)

    def onKeyCombo(self, event):
        """"""
        print("You pressed CTRL+Q!")

# Run the program
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyForm()
    frame.Show()
    app.MainLoop()