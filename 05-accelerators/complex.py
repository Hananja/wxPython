import wx


class MyForm(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None,
                          title="AcceleratorEntry Tutorial",
                          size=(500, 500))

        # Add a panel so it looks the correct on all platforms
        panel = wx.Panel(self, wx.ID_ANY)

        exit_menu_item = wx.MenuItem(id=wx.Window.NewControlId(), text="Exit",
                                     helpString="Exit the application")
        about_menu_item = wx.MenuItem(id=wx.Window.NewControlId(), text='About')

        menu = wx.Menu()
        menu.AppendItem(about_menu_item)
        menu.AppendSeparator()
        menu.AppendItem(exit_menu_item)

        menubar = wx.MenuBar()
        menubar.Append(menu, "&Menu")
        self.SetMenuBar(menubar)

        ID_NEW_WINDOW = wx.Window.NewControlId()
        ID_ABOUT = about_menu_item.GetId()

        self.Bind(wx.EVT_MENU, self.on_new_window, id=ID_NEW_WINDOW)
        self.Bind(wx.EVT_MENU, self.on_about, id=ID_ABOUT)

        entry_one = wx.AcceleratorEntry(wx.ACCEL_CTRL, ord('N'),
                                        ID_NEW_WINDOW,
                                        exit_menu_item)
        entry_two = wx.AcceleratorEntry(wx.ACCEL_SHIFT, ord('A'),
                                        ID_ABOUT,
                                        about_menu_item)
        entries = [entry_one, entry_two]

        accel_tbl = wx.AcceleratorTable(entries)
        self.SetAcceleratorTable(accel_tbl)

    def on_new_window(self, event):
        """"""
        print("You pressed CTRL+N!")

    def on_about(self, event):
        print('You pressed SHIFT+A')


# Run the program
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyForm()
    frame.Show()
    app.MainLoop()