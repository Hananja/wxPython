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

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		main_sizer = wx.BoxSizer( wx.VERTICAL )

		sub_sizer = wx.BoxSizer( wx.HORIZONTAL )


		sub_sizer.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.button_hello = wx.Button( self, wx.ID_ANY, u"Say Hello", wx.DefaultPosition, wx.DefaultSize, 0 )
		sub_sizer.Add( self.button_hello, 0, wx.ALIGN_BOTTOM|wx.ALL, 5 )


		main_sizer.Add( sub_sizer, 1, wx.ALIGN_RIGHT|wx.EXPAND, 5 )


		self.SetSizer( main_sizer )
		self.Layout()

		# Connect Events
		self.button_hello.Bind( wx.EVT_BUTTON, self.on_button_hello )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def on_button_hello( self, event ):
		event.Skip()


