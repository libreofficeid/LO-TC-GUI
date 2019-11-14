# -*- coding: utf-8 -*-
#!/usr/bin/env python

# =============================================================================
#
# Dialog implementation generated from a XDL file.
#
# Created: Sun Oct 27 04:10:08 2019
#      by: unodit 0.8.0
#
# WARNING! All changes made in this file will be overwritten
#          if the file is generated again!
#
# =============================================================================

import uno
import unohelper
from com.sun.star.awt import XActionListener, XMouseListener
from com.sun.star.task import XJobExecutor

import traceback

class SelectThemeListener(unohelper.Base, XMouseListener):
    def __init__(self, cast, context):
        self.cast = cast
        self.context = context

    def mousePressed(self, ev):
        if ev.ClickCount == 2:
            try:
                self.context.themeListBox_OnClick()
            except Exception as e:
                print(e)
                traceback.print_exc()
            return

class MainDialog_UI(unohelper.Base, XActionListener, XJobExecutor):
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

        self.DialogModel.Name = "ThemeChangerDialog"
        self.DialogModel.PositionX = "121"
        self.DialogModel.PositionY = "61"
        self.DialogModel.Width = 300
        self.DialogModel.Height = 200
        self.DialogModel.Closeable = True
        self.DialogModel.Moveable = True
        self.DialogModel.Title = "LibreOffice Theme Changer"

        
        # --------- create an instance of Button control, set properties ---
        self.createButton = self.DialogModel.createInstance("com.sun.star.awt.UnoControlButtonModel")

        self.createButton.Name = "createButton"
        self.createButton.TabIndex = 1
        self.createButton.PositionX = "10"
        self.createButton.PositionY = "180"
        self.createButton.Width = 64
        self.createButton.Height = 16
        self.createButton.Label = "Create New Theme"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("createButton", self.createButton)

        # add the action listener
        self.DialogContainer.getControl('createButton').addActionListener(self)
        self.DialogContainer.getControl('createButton').setActionCommand('createButton_OnClick')

        # --------- create an instance of Button control, set properties ---
        self.importButton = self.DialogModel.createInstance("com.sun.star.awt.UnoControlButtonModel")

        self.importButton.Name = "importButton"
        self.importButton.TabIndex = 1
        self.importButton.PositionX = "80"
        self.importButton.PositionY = "180"
        self.importButton.Width = 64
        self.importButton.Height = 16
        self.importButton.Label = "Import Theme"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("importButton", self.importButton)

        # add the action listener
        self.DialogContainer.getControl('importButton').addActionListener(self)
        self.DialogContainer.getControl('importButton').setActionCommand('importButton_OnClick')

        # --------- create an instance of Button control, set properties ---
        self.closeButton = self.DialogModel.createInstance("com.sun.star.awt.UnoControlButtonModel")

        self.closeButton.Name = "closeButton"
        self.closeButton.TabIndex = 0
        self.closeButton.PositionX = "220"
        self.closeButton.PositionY = "180"
        self.closeButton.Width = 64
        self.closeButton.Height = 16
        self.closeButton.Label = "Close"
        self.closeButton.PushButtonType = 2

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("closeButton", self.closeButton)

        # add the action listener
        self.DialogContainer.getControl('closeButton').addActionListener(self)
        self.DialogContainer.getControl('closeButton').setActionCommand('closeButton_OnClick')

        # --------- create an instance of ListBox control, set properties ---
        self.themeListBox = self.DialogModel.createInstance("com.sun.star.awt.UnoControlListBoxModel")

        self.themeListBox.Name = "themeListBox"
        self.themeListBox.TabIndex = 2
        self.themeListBox.PositionX = "11"
        self.themeListBox.PositionY = "31"
        self.themeListBox.Width = 274
        self.themeListBox.Height = 142

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("themeListBox", self.themeListBox)

        # add the action listener
        self.DialogContainer.getControl('themeListBox').addMouseListener(SelectThemeListener(self.DialogContainer,self))

        # --------- create an instance of FixedText control, set properties ---
        self.lotcLabel = self.DialogModel.createInstance("com.sun.star.awt.UnoControlFixedTextModel")

        self.lotcLabel.Name = "lotcLabel"
        self.lotcLabel.TabIndex = 3
        self.lotcLabel.PositionX = "11"
        self.lotcLabel.PositionY = "5"
        self.lotcLabel.Width = 260
        self.lotcLabel.Height = 24
        self.lotcLabel.Label = "Welcome to LibreOffice Theme Changer.\nPlease choose theme you like than hit apply.\nOr you can import your own theme using Import Theme button."

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("lotcLabel", self.lotcLabel)

        # get os env
        self.register_new_item(self.LocalContext)

    # -----------------------------------------------------------
    #               Action events
    # -----------------------------------------------------------

    def actionPerformed(self, oActionEvent):

        if oActionEvent.ActionCommand == 'createButton_OnClick':
            self.createButton_OnClick()
        
        if oActionEvent.ActionCommand == 'importButton_OnClick':
            self.importButton_OnClick()

        if oActionEvent.ActionCommand == 'closeButton_OnClick':
            self.closeButton_OnClick()

    def themeListBox_OnClick(self):
        # will be override in main
        pass

    def register_new_item(self, ctx, path_to_file=None):
        # will be override on main
        pass

    def clear_theme_list(self):
        # will be override on main
        pass

    def create_new_component(self, name, thumbnail_full_path=''):
        # will be override on main
        pass

# ----------------- END GENERATED CODE ----------------------------------------