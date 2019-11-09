# -*- coding: utf-8 -*-
#!/usr/bin/env python

# =============================================================================
#
# Dialog implementation generated from a XDL file.
#
# Created: Sun Oct 27 04:11:08 2019
#      by: unodit 0.8.0
#
# WARNING! All changes made in this file will be overwritten
#          if the file is generated again!
#
# =============================================================================

import uno
import unohelper
from com.sun.star.awt import XActionListener
from com.sun.star.task import XJobExecutor


class CreateDialog_UI(unohelper.Base, XActionListener, XJobExecutor):
    """
    Class documentation...AAAAAAAAAAAAAAAAAAAAAAA
    """
    def __init__(self, ctx=uno.getComponentContext()):
        self.LocalContext = ctx
        self.ServiceManager = self.LocalContext.ServiceManager
        self.Toolkit = self.ServiceManager.createInstanceWithContext("com.sun.star.awt.ExtToolkit", self.LocalContext)

        # -----------------------------------------------------------
        #               Create dialog and insert controls
        # -----------------------------------------------------------

        # --------------create dialog container and set model and properties
        self.DialogContainer = self.ServiceManager.createInstanceWithContext("com.sun.star.awt.UnoControlDialog", self.LocalContext)
        self.DialogModel = self.ServiceManager.createInstance("com.sun.star.awt.UnoControlDialogModel")
        self.DialogContainer.setModel(self.DialogModel)

        self.DialogModel.Name = "ThemeChangerCreate"
        self.DialogModel.PositionX = "136"
        self.DialogModel.PositionY = "59"
        self.DialogModel.Width = 175
        self.DialogModel.Height = 152
        self.DialogModel.Closeable = True
        self.DialogModel.Moveable = True
        self.DialogModel.Title = "Create New Theme"

        
        # --------- create an instance of FixedText control, set properties ---
        self.Label1 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlFixedTextModel")

        self.Label1.Name = "Label1"
        self.Label1.TabIndex = 0
        self.Label1.PositionX = "10"
        self.Label1.PositionY = "52"
        self.Label1.Width = 38
        self.Label1.Height = 10
        self.Label1.Label = "Theme Name"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("Label1", self.Label1)

        # --------- create an instance of FixedText control, set properties ---
        self.Label2 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlFixedTextModel")

        self.Label2.Name = "Label2"
        self.Label2.TabIndex = 4
        self.Label2.PositionX = "10"
        self.Label2.PositionY = "90"
        self.Label2.Width = 43
        self.Label2.Height = 10
        self.Label2.Label = "Theme Location"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("Label2", self.Label2)

        # --------- create an instance of FixedText control, set properties ---
        self.Label3 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlFixedTextModel")

        self.Label3.Name = "Label3"
        self.Label3.TabIndex = 5
        self.Label3.PositionX = "10"
        self.Label3.PositionY = "76"
        self.Label3.Width = 154
        self.Label3.Height = 8
        self.Label3.Label = "Insert your theme name here"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("Label3", self.Label3)

        # --------- create an instance of FixedText control, set properties ---
        self.Label4 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlFixedTextModel")

        self.Label4.Name = "Label4"
        self.Label4.TabIndex = 7
        self.Label4.PositionX = "10"
        self.Label4.PositionY = "113"
        self.Label4.Width = 154
        self.Label4.Height = 8
        self.Label4.Label = "Save path for placing your new theme"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("Label4", self.Label4)

        # --------- create an instance of FixedText control, set properties ---
        self.Label5 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlFixedTextModel")

        self.Label5.Name = "Label5"
        self.Label5.TabIndex = 9
        self.Label5.PositionX = "10"
        self.Label5.PositionY = "15"
        self.Label5.Width = 38
        self.Label5.Height = 10
        self.Label5.Label = "Author"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("Label5", self.Label5)

        # --------- create an instance of FixedText control, set properties ---
        self.Label6 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlFixedTextModel")

        self.Label6.Name = "Label6"
        self.Label6.TabIndex = 11
        self.Label6.PositionX = "10"
        self.Label6.PositionY = "40"
        self.Label6.Width = 154
        self.Label6.Height = 8
        self.Label6.Label = "Insert your name here"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("Label6", self.Label6)

        # --------- create an instance of FileControl control, set properties ---
        self.FileControl1 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlFileControlModel")

        self.FileControl1.Name = "FileControl1"
        self.FileControl1.TabIndex = 2
        self.FileControl1.PositionX = "10"
        self.FileControl1.PositionY = "100"
        self.FileControl1.Width = 156
        self.FileControl1.Height = 12

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("FileControl1", self.FileControl1)

        # --------- create an instance of Edit control, set properties ---
        self.TextField1 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlEditModel")

        self.TextField1.Name = "TextField1"
        self.TextField1.TabIndex = 3
        self.TextField1.PositionX = "10"
        self.TextField1.PositionY = "64"
        self.TextField1.Width = 155
        self.TextField1.Height = 12

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("TextField1", self.TextField1)

        # --------- create an instance of Edit control, set properties ---
        self.TextField2 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlEditModel")

        self.TextField2.Name = "TextField2"
        self.TextField2.TabIndex = 10
        self.TextField2.PositionX = "10"
        self.TextField2.PositionY = "26"
        self.TextField2.Width = 155
        self.TextField2.Height = 12

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("TextField2", self.TextField2)

        # --------- create an instance of Button control, set properties ---
        self.CommandButton1 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlButtonModel")

        self.CommandButton1.Name = "CommandButton1"
        self.CommandButton1.TabIndex = 6
        self.CommandButton1.PositionX = "85"
        self.CommandButton1.PositionY = "134"
        self.CommandButton1.Width = 59
        self.CommandButton1.Height = 13
        self.CommandButton1.Label = "Create"
        self.CommandButton1.PushButtonType = 1

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("CommandButton1", self.CommandButton1)

        # add the action listener
        self.DialogContainer.getControl('CommandButton1').addActionListener(self)
        self.DialogContainer.getControl('CommandButton1').setActionCommand('CommandButton1_OnClick')

        # --------- create an instance of Button control, set properties ---
        self.CommandButton2 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlButtonModel")

        self.CommandButton2.Name = "CommandButton2"
        self.CommandButton2.TabIndex = 8
        self.CommandButton2.PositionX = "23"
        self.CommandButton2.PositionY = "134"
        self.CommandButton2.Width = 59
        self.CommandButton2.Height = 13
        self.CommandButton2.Label = "Cancel"
        self.CommandButton2.PushButtonType = 2

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("CommandButton2", self.CommandButton2)

        # add the action listener
        self.DialogContainer.getControl('CommandButton2').addActionListener(self)
        self.DialogContainer.getControl('CommandButton2').setActionCommand('CommandButton2_OnClick')

        # --------- create an instance of GroupBox control, set properties ---
        self.FrameControl1 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlGroupBoxModel")

        self.FrameControl1.Name = "FrameControl1"
        self.FrameControl1.TabIndex = 1
        self.FrameControl1.PositionX = "3"
        self.FrameControl1.PositionY = "3"
        self.FrameControl1.Width = 168
        self.FrameControl1.Height = 128
        self.FrameControl1.Label = "Create New Theme"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("FrameControl1", self.FrameControl1)

    # -----------------------------------------------------------
    #               Action events
    # -----------------------------------------------------------

    def actionPerformed(self, oActionEvent):
        
        if oActionEvent.ActionCommand == 'CommandButton1_OnClick':
            self.CommandButton1_OnClick()

        if oActionEvent.ActionCommand == 'CommandButton2_OnClick':
            self.CommandButton2_OnClick()


# ----------------- END GENERATED CODE ----------------------------------------