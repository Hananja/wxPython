# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
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

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 605,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		main_sizer = wx.BoxSizer( wx.VERTICAL )

		sub_sizer = wx.BoxSizer( wx.HORIZONTAL )

		self.input_label = wx.StaticText( self, wx.ID_ANY, u"Name:", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.input_label.Wrap( -1 )

		sub_sizer.Add( self.input_label, 1, wx.ALL, 5 )

		self.name_input = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		sub_sizer.Add( self.name_input, 2, wx.ALL, 5 )

		self.hello_button = wx.Button( self, wx.ID_ANY, u"Go", wx.DefaultPosition, wx.DefaultSize, 0 )
		sub_sizer.Add( self.hello_button, 1, wx.ALL, 5 )


		main_sizer.Add( sub_sizer, 0, wx.EXPAND, 5 )


		self.SetSizer( main_sizer )
		self.Layout()

		# Connect Events
		self.name_input.Bind( wx.EVT_TEXT_ENTER, self.on_text_enter )
		self.hello_button.Bind( wx.EVT_BUTTON, self.on_button_click )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def on_text_enter( self, event ):
		event.Skip()

	def on_button_click( self, event ):
		event.Skip()


