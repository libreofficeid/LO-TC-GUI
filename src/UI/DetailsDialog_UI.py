# -*- coding: utf-8 -*-
#!/usr/bin/env python

# =============================================================================
#
# Dialog implementation generated from a XDL file.
#
# Created: Sun Oct 27 04:11:43 2019
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


class DetailsDialog_UI(unohelper.Base, XActionListener, XJobExecutor):
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

        self.DialogModel.Name = "ThemeChangerDetails"
        self.DialogModel.PositionX = "121"
        self.DialogModel.PositionY = "61"
        self.DialogModel.Width = 250
        self.DialogModel.Height = 180
        self.DialogModel.Closeable = True
        self.DialogModel.Moveable = True
        self.DialogModel.Title = "My Theme - Details"

        
        # --------- create an instance of ImageControl control, set properties ---
        self.ImageControl1 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlImageControlModel")

        self.ImageControl1.Name = "ImageControl1"
        self.ImageControl1.TabIndex = 0
        self.ImageControl1.PositionX = "4"
        self.ImageControl1.PositionY = "4"
        self.ImageControl1.Width = 240
        self.ImageControl1.Height = 100

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("ImageControl1", self.ImageControl1)

        # --------- create an instance of Edit control, set properties ---
        self.TextField1 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlEditModel")

        self.TextField1.Name = "TextField1"
        self.TextField1.TabIndex = 1
        self.TextField1.PositionX = "4"
        self.TextField1.PositionY = "110"
        self.TextField1.Width = 178
        self.TextField1.Height = 60

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("TextField1", self.TextField1)

        # --------- create an instance of ComboBox control, set properties ---
        self.ComboBox1 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlComboBoxModel")

        self.ComboBox1.Name = "ComboBox1"
        self.ComboBox1.TabIndex = 2
        self.ComboBox1.PositionX = "193"
        self.ComboBox1.PositionY = "112"
        self.ComboBox1.Width = 53
        self.ComboBox1.Height = 12
        self.ComboBox1.StringItemList = ('p', 'r', 'e', 'v', 'i', 'e', 'w', ' ', '1')
        self.ComboBox1.Dropdown = True

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("ComboBox1", self.ComboBox1)

        # --------- create an instance of Button control, set properties ---
        self.CommandButton1 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlButtonModel")

        self.CommandButton1.Name = "CommandButton1"
        self.CommandButton1.TabIndex = 3
        self.CommandButton1.PositionX = "207"
        self.CommandButton1.PositionY = "131"
        self.CommandButton1.Width = 38
        self.CommandButton1.Height = 17
        self.CommandButton1.Label = "Apply"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("CommandButton1", self.CommandButton1)

        # add the action listener
        self.DialogContainer.getControl('CommandButton1').addActionListener(self)
        self.DialogContainer.getControl('CommandButton1').setActionCommand('CommandButton1_OnClick')

        # --------- create an instance of Button control, set properties ---
        self.CommandButton2 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlButtonModel")

        self.CommandButton2.Name = "CommandButton2"
        self.CommandButton2.TabIndex = 4
        self.CommandButton2.PositionX = "207"
        self.CommandButton2.PositionY = "154"
        self.CommandButton2.Width = 38
        self.CommandButton2.Height = 17
        self.CommandButton2.Label = "Remove"

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