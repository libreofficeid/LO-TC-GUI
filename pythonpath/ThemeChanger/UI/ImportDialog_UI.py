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
from com.sun.star.awt import XActionListener, XKeyListener, XMouseListener
from com.sun.star.task import XJobExecutor


class ImportDialog_UI(unohelper.Base, XActionListener, XKeyListener, XMouseListener, XJobExecutor):
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
        self.DialogModel.PositionX = "50"
        self.DialogModel.PositionY = "50"
        self.DialogModel.Width = 175
        self.DialogModel.Height = 83
        self.DialogModel.Closeable = True
        self.DialogModel.Moveable = True
        self.DialogModel.Title = "Import Theme"

        
        # --------- create an instance of FileControl control, set properties ---
        self.LotcLocation = self.DialogModel.createInstance("com.sun.star.awt.UnoControlEditModel")

        self.LotcLocation.Name = "LotcLocation"
        self.LotcLocation.TabIndex = 0
        self.LotcLocation.PositionX = "9"
        self.LotcLocation.PositionY = "27"
        self.LotcLocation.Width = 156
        self.LotcLocation.Height = 12

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("LotcLocation", self.LotcLocation)
        self.DialogContainer.getControl("LotcLocation").addMouseListener(self)
        self.DialogContainer.getControl("LotcLocation").addKeyListener(self)

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
        self.importButton = self.DialogModel.createInstance("com.sun.star.awt.UnoControlButtonModel")

        self.importButton.Name = "importButton"
        self.importButton.TabIndex = 2
        self.importButton.PositionX = "88"
        self.importButton.PositionY = "60"
        self.importButton.Width = 59
        self.importButton.Height = 13
        self.importButton.Label = "Import"
        self.importButton.PushButtonType = 1

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("importButton", self.importButton)

        # --------- create an instance of Button control, set properties ---
        self.cancelButton = self.DialogModel.createInstance("com.sun.star.awt.UnoControlButtonModel")

        self.cancelButton.Name = "cancelButton"
        self.cancelButton.TabIndex = 4
        self.cancelButton.PositionX = "26"
        self.cancelButton.PositionY = "60"
        self.cancelButton.Width = 59
        self.cancelButton.Height = 13
        self.cancelButton.Label = "Cancel"
        self.cancelButton.PushButtonType = 2

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("cancelButton", self.cancelButton)

    def mousePressed(self, evt):
        self.pick_lotc()

    def keyPressed(self, evt):
        self.pick_lotc()

# ----------------- END GENERATED CODE ----------------------------------------