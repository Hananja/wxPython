# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Nov 15 2019)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class AbstractMainPanel
###########################################################################

class AbstractMainPanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		main_sizer = wx.BoxSizer( wx.VERTICAL )

		input_sizer = wx.BoxSizer( wx.HORIZONTAL )

		self.add_label = wx.StaticText( self, wx.ID_ANY, u"Hinzufügen:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.add_label.Wrap( -1 )

		input_sizer.Add( self.add_label, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.input_text = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		input_sizer.Add( self.input_text, 1, wx.ALL, 5 )

		self.add_button = wx.Button( self, wx.ID_ANY, u"Hinzufügen", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.add_button.SetDefault()
		self.add_button.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		input_sizer.Add( self.add_button, 0, wx.ALL, 5 )


		main_sizer.Add( input_sizer, 0, wx.EXPAND, 5 )

		self.main_list = wx.ListBox( self, wx.ID_ANY )
		main_sizer.Add( self.main_list, 1, wx.ALL|wx.EXPAND, 5 )

		button_sizer = wx.BoxSizer( wx.HORIZONTAL )

		self.delete_button = wx.Button( self, wx.ID_ANY, u"Löschen", wx.DefaultPosition, wx.DefaultSize, 0 )
		button_sizer.Add( self.delete_button, 0, wx.ALL, 5 )


		button_sizer.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.quit_button = wx.Button( self, wx.ID_ANY, u"Schließen", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.quit_button.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		button_sizer.Add( self.quit_button, 0, wx.ALL, 5 )


		main_sizer.Add( button_sizer, 0, wx.EXPAND, 5 )


		self.SetSizer( main_sizer )
		self.Layout()

		# Connect Events
		self.input_text.Bind( wx.EVT_TEXT_ENTER, self.on_input_text_enter )
		self.add_button.Bind( wx.EVT_BUTTON, self.on_button_add )
		self.delete_button.Bind( wx.EVT_BUTTON, self.on_button_delete )
		self.quit_button.Bind( wx.EVT_BUTTON, self.on_button_quit )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def on_input_text_enter( self, event ):
		event.Skip()

	def on_button_add( self, event ):
		event.Skip()

	def on_button_delete( self, event ):
		event.Skip()

	def on_button_quit( self, event ):
		event.Skip()


