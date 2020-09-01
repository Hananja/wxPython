# First things, first. Import the wxPython package.
import wx

# import generated class
from generated import AbstractMainPanel


class MainPanel(AbstractMainPanel):
    # override event handler
    def on_button_hello(self, event):
        print("Hello World.")

# Next, create an application object.
app = wx.App()

# Then a frame.
frm = wx.Frame(None, title="Hello World")
# with our custom panel
pnl = MainPanel(frm)

# Show it.
frm.Show()

# Start the event loop.
app.MainLoop()
