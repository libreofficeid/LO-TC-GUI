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
from com.sun.star.awt import XActionListener, XMouseListener, XKeyListener
from com.sun.star.task import XJobExecutor


class CreateDialog_UI(unohelper.Base, XActionListener, XMouseListener, XKeyListener, XJobExecutor):
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
        self.DialogModel.PositionX = "50"
        self.DialogModel.PositionY = "30"
        self.DialogModel.Width = 175
        self.DialogModel.Height = 140
        self.DialogModel.Closeable = True
        self.DialogModel.Moveable = True
        self.DialogModel.Title = "Create New Theme"

        
        # --------- create an instance of FixedText control, set properties ---
        self.Label1 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlFixedTextModel")

        self.Label1.Name = "Label1"
        self.Label1.TabIndex = 0
        self.Label1.PositionX = "10"
        self.Label1.PositionY = "45"
        self.Label1.Width = 150
        self.Label1.Height = 10
        self.Label1.Label = "Theme Name (e.g Awesome Theme)"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("Label1", self.Label1)

        # --------- create an instance of FixedText control, set properties ---
        self.Label2 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlFixedTextModel")

        self.Label2.Name = "Label2"
        self.Label2.TabIndex = 10
        self.Label2.PositionX = "10"
        self.Label2.PositionY = "77"
        self.Label2.Width = 150
        self.Label2.Height = 10
        self.Label2.Label = "Path to Save This Theme"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("Label2", self.Label2)

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

        # --------- create an instance of FileControl control, set properties ---
        # self.NewThemeFolderField = self.DialogModel.createInstance("com.sun.star.awt.UnoControlFileControlModel")
        self.NewThemeFolderField = self.DialogModel.createInstance("com.sun.star.awt.UnoControlEditModel")

        self.NewThemeFolderField.Name = "NewThemeFolderField"
        self.NewThemeFolderField.TabIndex = 4
        self.NewThemeFolderField.PositionX = "10"
        self.NewThemeFolderField.PositionY = "87"
        self.NewThemeFolderField.Width = 130
        self.NewThemeFolderField.Height = 12

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("NewThemeFolderField", self.NewThemeFolderField)
        self.DialogContainer.getControl("NewThemeFolderField").addMouseListener(self)
        self.DialogContainer.getControl("NewThemeFolderField").addKeyListener(self)

        # --------- create an instance of Edit control, set properties ---
        self.ThemeNameField = self.DialogModel.createInstance("com.sun.star.awt.UnoControlEditModel")

        self.ThemeNameField.Name = "ThemeNameField"
        self.ThemeNameField.TabIndex = 3
        self.ThemeNameField.PositionX = "10"
        self.ThemeNameField.PositionY = "57"
        self.ThemeNameField.Width = 155
        self.ThemeNameField.Height = 12

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("ThemeNameField", self.ThemeNameField)

        # --------- create an instance of Edit control, set properties ---
        self.AuthorNameField = self.DialogModel.createInstance("com.sun.star.awt.UnoControlEditModel")

        self.AuthorNameField.Name = "AuthorNameField"
        self.AuthorNameField.TabIndex = 2
        self.AuthorNameField.PositionX = "10"
        self.AuthorNameField.PositionY = "26"
        self.AuthorNameField.Width = 155
        self.AuthorNameField.Height = 12

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("AuthorNameField", self.AuthorNameField)

        # --------- create an instance of Button control, set properties ---
        self.CreateButton = self.DialogModel.createInstance("com.sun.star.awt.UnoControlButtonModel")

        self.CreateButton.Name = "CreateButton"
        self.CreateButton.TabIndex = 6
        self.CreateButton.PositionX = "90"
        self.CreateButton.PositionY = "120"
        self.CreateButton.Width = 59
        self.CreateButton.Height = 13
        self.CreateButton.Label = "Create"
        self.CreateButton.PushButtonType = 1

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("CreateButton", self.CreateButton)

        # # add the action listener
        # self.DialogContainer.getControl('CreateButton').addActionListener(self)
        # self.DialogContainer.getControl('CreateButton').setActionCommand('CreateButton_OnClick')

        # --------- create an instance of Button control, set properties ---
        self.CancelButton = self.DialogModel.createInstance("com.sun.star.awt.UnoControlButtonModel")

        self.CancelButton.Name = "CancelButton"
        self.CancelButton.TabIndex = 8
        self.CancelButton.PositionX = "25"
        self.CancelButton.PositionY = "120"
        self.CancelButton.Width = 59
        self.CancelButton.Height = 13
        self.CancelButton.Label = "Cancel"
        self.CancelButton.PushButtonType = 2

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("CancelButton", self.CancelButton)

        # # add the action listener
        # self.DialogContainer.getControl('CancelButton').addActionListener(self)
        # self.DialogContainer.getControl('CancelButton').setActionCommand('CancelButton_OnClick')

        # --------- create an instance of Button control, set properties ---

        self.BrowseButton = self.DialogModel.createInstance("com.sun.star.awt.UnoControlButtonModel")

        self.BrowseButton.Name = "BrowseButton"
        self.BrowseButton.TabIndex = 3
        self.BrowseButton.PositionX = "141"
        self.BrowseButton.PositionY = "86"
        self.BrowseButton.Width = 24
        self.BrowseButton.Height = 14
        self.BrowseButton.Label = "Browse"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("BrowseButton", self.BrowseButton)
        self.DialogContainer.getControl('BrowseButton').addActionListener(self)
        self.DialogContainer.getControl('BrowseButton').setActionCommand('BrowseButton_OnClick')

        # --------- create an instance of GroupBox control, set properties ---
        self.FrameControl1 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlGroupBoxModel")

        self.FrameControl1.Name = "FrameControl1"
        self.FrameControl1.TabIndex = 1
        self.FrameControl1.PositionX = "3"
        self.FrameControl1.PositionY = "3"
        self.FrameControl1.Width = 168
        self.FrameControl1.Height = 110
        self.FrameControl1.Label = "Create New Theme"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("FrameControl1", self.FrameControl1)

    # -----------------------------------------------------------
    #               Action events
    # -----------------------------------------------------------
    def actionPerformed(self, oActionEvent):
        if oActionEvent.ActionCommand == 'BrowseButton_OnClick':
            self.pick_folder()

    def mousePressed(self, evt):
        self.pick_folder()

    def keyPressed(self, evt):
        self.pick_folder()

# ----------------- END GENERATED CODE ----------------------------------------