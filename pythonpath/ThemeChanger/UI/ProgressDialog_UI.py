# -*- coding: utf-8 -*-
#!/usr/bin/env python3

# =============================================================================
#
# Dialog implementation generated from a XDL file.
#
# Created: Sun Oct 27 04:12:04 2019
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


class ProgressDialog_UI(unohelper.Base, XActionListener, XJobExecutor):
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

        self.DialogModel.Name = "ThemeChangerProgress"
        self.DialogModel.PositionX = "136"
        self.DialogModel.PositionY = "60"
        self.DialogModel.Width = 175
        self.DialogModel.Height = 48
        self.DialogModel.Closeable = True
        self.DialogModel.Moveable = True
        self.DialogModel.Title = "Progress Name Here"

        
        # --------- create an instance of ProgressBar control, set properties ---
        self.ProgressBar1 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlProgressBarModel")

        self.ProgressBar1.Name = "ProgressBar1"
        self.ProgressBar1.TabIndex = 0
        self.ProgressBar1.PositionX = "3"
        self.ProgressBar1.PositionY = "23"
        self.ProgressBar1.Width = 164
        self.ProgressBar1.Height = 13
        self.ProgressBar1.ProgressValue = 50

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("ProgressBar1", self.ProgressBar1)

        # --------- create an instance of FixedText control, set properties ---
        self.Label1 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlFixedTextModel")

        self.Label1.Name = "Label1"
        self.Label1.TabIndex = 1
        self.Label1.PositionX = "8"
        self.Label1.PositionY = "6"
        self.Label1.Width = 65
        self.Label1.Height = 10
        self.Label1.Label = "Progress Description"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("Label1", self.Label1)

    # -----------------------------------------------------------
    #               Action events
    # -----------------------------------------------------------

    def actionPerformed(self, oActionEvent):
        pass

# ----------------- END GENERATED CODE ----------------------------------------