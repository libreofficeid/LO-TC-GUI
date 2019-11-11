# -*- coding: utf-8 -*-
#!/usr/bin/env python

# =============================================================================
#
# Dialog implementation generated from a XDL file.
#
# Created: Sun Oct 27 04:12:23 2019
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


class CompleteDialog_UI(unohelper.Base, XActionListener, XJobExecutor):
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

        self.DialogModel.Name = "ThemeChangerComplete"
        self.DialogModel.PositionX = "136"
        self.DialogModel.PositionY = "60"
        self.DialogModel.Width = 136
        self.DialogModel.Height = 84
        self.DialogModel.Closeable = True
        self.DialogModel.Moveable = True
        self.DialogModel.Title = "Completed - Event Name"

        
        # --------- create an instance of FixedText control, set properties ---
        self.Label2 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlFixedTextModel")

        self.Label2.Name = "Label2"
        self.Label2.TabIndex = 0
        self.Label2.PositionX = "3"
        self.Label2.PositionY = "4"
        self.Label2.Width = 129
        self.Label2.Height = 54
        self.Label2.Label = "Post-progress description here"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("Label2", self.Label2)

        # --------- create an instance of Button control, set properties ---
        self.CommandButton1 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlButtonModel")

        self.CommandButton1.Name = "CommandButton1"
        self.CommandButton1.TabIndex = 1
        self.CommandButton1.PositionX = "53"
        self.CommandButton1.PositionY = "65"
        self.CommandButton1.Width = 32
        self.CommandButton1.Height = 15
        self.CommandButton1.Label = "OK"
        self.CommandButton1.PushButtonType = 1

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("CommandButton1", self.CommandButton1)

        # add the action listener
        self.DialogContainer.getControl('CommandButton1').addActionListener(self)
        self.DialogContainer.getControl('CommandButton1').setActionCommand('CommandButton1_OnClick')

    # -----------------------------------------------------------
    #               Action events
    # -----------------------------------------------------------

    def actionPerformed(self, oActionEvent):
        
        if oActionEvent.ActionCommand == 'CommandButton1_OnClick':
            self.CommandButton1_OnClick()


# ----------------- END GENERATED CODE ----------------------------------------