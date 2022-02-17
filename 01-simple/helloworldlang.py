#!/usr/bin/env python
"""
Hello World, but with more meat and multi language support
"""

import wx

hello_text = {
    "english": "Hello world!",
    "german": "Hallo welt!",
    "france": "Bonjour le monde!",
    "arabic": "مرحبا بالعالم"
}

class HelloFrame(wx.Frame):
    """
    A Frame that says Hello World
    """

    def __init__(self, *args, **kw):
        """
        Constructor for Frame class
        :param args: list of positional parameters, see wx.Frame
        :param kw: dictionary of keyword parameters, see wx.Frame
        """
        # ensure the parent's __init__ (inheritance) is called
        super(HelloFrame, self).__init__(*args, **kw)

        # create a panel in the frame
        pnl = wx.Panel(self)

        # put some text with a larger bold font on it
        self.static_text = wx.StaticText(pnl, label=hello_text["english"])
        font = self.static_text.GetFont()
        font.PointSize += 10
        font = font.Bold()
        self.static_text.SetFont(font)

        # and create a sizer to manage the layout of child widgets
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.static_text, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
        pnl.SetSizer(sizer)

        # create a menu bar
        self.makeMenuBar()

        # and a status bar
        self.CreateStatusBar()
        self.SetStatusText("Welcome to wxPython!")


    def makeMenuBar(self):
        """
        A menu bar is composed of menus, which are composed of menu items.
        This method builds a set of menus and binds handlers to be called
        when the menu item is selected.
        """

        # Make a file menu with Hello and Exit items
        fileMenu = wx.Menu()
        # The "\t..." syntax defines an accelerator key that also triggers
        # the same event
        helloItem = fileMenu.Append(-1, "&Hello...\tCtrl-H",
                "Help string shown in status bar for this menu item")
        settingsItem = fileMenu.Append(-1, "&Settings...", "Modify application settings")
        fileMenu.AppendSeparator()
        # When using a stock ID we don't need to specify the menu item's
        # label
        exitItem = fileMenu.Append(wx.ID_EXIT)

        # Now a help menu for the about item
        helpMenu = wx.Menu()
        aboutItem = helpMenu.Append(wx.ID_ABOUT)

        # Make the menu bar and add the two menus to it. The '&' defines
        # that the next letter is the "mnemonic" for the menu item. On the
        # platforms that support it those letters are underlined and can be
        # triggered from the keyboard.
        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        menuBar.Append(helpMenu, "&Help")

        # Give the menu bar to the frame
        self.SetMenuBar(menuBar)

        # Finally, associate a handler function with the EVT_MENU event for
        # each of the menu items. That means that when that menu item is
        # activated then the associated handler function will be called.
        self.Bind(wx.EVT_MENU, self.OnHello, helloItem)
        self.Bind(wx.EVT_MENU, self.OnExit,  exitItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)
        self.Bind(wx.EVT_MENU, self.OnSettings, settingsItem)

    def OnSettings(self, event):
        """ Show settings dialog """
        choices = list(hello_text.keys())
        dlg = wx.SingleChoiceDialog(self, "Please select language", "Language selection", choices)
        buttom = dlg.ShowModal()
        if wx.ID_OK == buttom:
            self.static_text.SetLabelText(hello_text[choices[dlg.GetSelection()]])

    def OnExit(self, event):
        """Close the frame, terminating the application."""
        self.Close(True)


    def OnHello(self, event):
        """Say hello to the user."""
        wx.MessageBox("Hello again from wxPython")


    def OnAbout(self, event):
        """Display an About Dialog"""
        wx.MessageBox("This is a wxPython Hello World sample",
                      "About Hello World 2",
                      wx.OK|wx.ICON_INFORMATION)


if __name__ == '__main__': # quick and ditry: Do not run on module import
    # When this module is run (not imported) then create the app, the
    # frame, show it, and start the event loop.
    app = wx.App()
    frm = HelloFrame(None, title='Hello World Multilanguage')
    frm.Show()
    app.MainLoop()
