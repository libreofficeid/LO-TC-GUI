# -*- coding: utf-8 -*-
#!/usr/bin/env python

# =============================================================================
#
# Dialog implementation generated from a XDL file.
#
# Created: Sun Oct 27 04:11:25 2019
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


class ImportDialog_UI(unohelper.Base, XActionListener, XJobExecutor):
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

        self.DialogModel.Name = "ThemeChangerImport"
        self.DialogModel.PositionX = "136"
        self.DialogModel.PositionY = "65"
        self.DialogModel.Width = 175
        self.DialogModel.Height = 83
        self.DialogModel.Closeable = True
        self.DialogModel.Moveable = True
        self.DialogModel.Title = "Import Theme"

        
        # --------- create an instance of FileControl control, set properties ---
        self.FileControl1 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlFileControlModel")

        self.FileControl1.Name = "FileControl1"
        self.FileControl1.TabIndex = 0
        self.FileControl1.PositionX = "9"
        self.FileControl1.PositionY = "27"
        self.FileControl1.Width = 156
        self.FileControl1.Height = 12

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("FileControl1", self.FileControl1)

        # --------- create an instance of FixedText control, set properties ---
        self.Label2 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlFixedTextModel")

        self.Label2.Name = "Label2"
        self.Label2.TabIndex = 1
        self.Label2.PositionX = "9"
        self.Label2.PositionY = "13"
        self.Label2.Width = 43
        self.Label2.Height = 10
        self.Label2.Label = "Theme Location"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("Label2", self.Label2)

        # --------- create an instance of FixedText control, set properties ---
        self.Label4 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlFixedTextModel")

        self.Label4.Name = "Label4"
        self.Label4.TabIndex = 3
        self.Label4.PositionX = "9"
        self.Label4.PositionY = "40"
        self.Label4.Width = 154
        self.Label4.Height = 8
        self.Label4.Label = "Locate your *.lotc file to import theme"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("Label4", self.Label4)

        # --------- create an instance of Button control, set properties ---
        self.CommandButton1 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlButtonModel")

        self.CommandButton1.Name = "CommandButton1"
        self.CommandButton1.TabIndex = 2
        self.CommandButton1.PositionX = "88"
        self.CommandButton1.PositionY = "60"
        self.CommandButton1.Width = 59
        self.CommandButton1.Height = 13
        self.CommandButton1.Label = "Import"
        self.CommandButton1.PushButtonType = 1

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("CommandButton1", self.CommandButton1)

        # add the action listener
        self.DialogContainer.getControl('CommandButton1').addActionListener(self)
        self.DialogContainer.getControl('CommandButton1').setActionCommand('CommandButton1_OnClick')

        # --------- create an instance of Button control, set properties ---
        self.CommandButton2 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlButtonModel")

        self.CommandButton2.Name = "CommandButton2"
        self.CommandButton2.TabIndex = 4
        self.CommandButton2.PositionX = "26"
        self.CommandButton2.PositionY = "60"
        self.CommandButton2.Width = 59
        self.CommandButton2.Height = 13
        self.CommandButton2.Label = "Cancel"
        self.CommandButton2.PushButtonType = 2

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("CommandButton2", self.CommandButton2)

        # add the action listener
        self.DialogContainer.getControl('CommandButton2').addActionListener(self)
        self.DialogContainer.getControl('CommandButton2').setActionCommand('CommandButton2_OnClick')

    # -----------------------------------------------------------
    #               Action events
    # -----------------------------------------------------------

    def actionPerformed(self, oActionEvent):
        
        if oActionEvent.ActionCommand == 'CommandButton1_OnClick':
            self.CommandButton1_OnClick()

        if oActionEvent.ActionCommand == 'CommandButton2_OnClick':
            self.CommandButton2_OnClick()


# ----------------- END GENERATED CODE ----------------------------------------