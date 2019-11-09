# -*- coding: utf-8 -*-
#!/usr/bin/env python

import uno
from com.sun.star.awt.MessageBoxButtons import BUTTONS_OK, BUTTONS_OK_CANCEL, BUTTONS_YES_NO, BUTTONS_YES_NO_CANCEL, BUTTONS_RETRY_CANCEL, BUTTONS_ABORT_IGNORE_RETRY
from com.sun.star.awt.MessageBoxButtons import DEFAULT_BUTTON_OK, DEFAULT_BUTTON_CANCEL, DEFAULT_BUTTON_RETRY, DEFAULT_BUTTON_YES, DEFAULT_BUTTON_NO, DEFAULT_BUTTON_IGNORE
from com.sun.star.awt.MessageBoxType import MESSAGEBOX, INFOBOX, WARNINGBOX, ERRORBOX, QUERYBOX
from UI.MainDialog_UI import MainDialog_UI
from ImportDialog import ImportDialog
from CreateDialog import CreateDialog


class MainDialog(MainDialog_UI):
    '''
    Class documentation...
    '''
    def __init__(self, ctx=uno.getComponentContext(), **kwargs):

        self.ctx = ctx
        MainDialog_UI.__init__(self, self.ctx)

        # for key, value in kwargs.items():
            # if key == 'document':
            # self.document = value

        # --------- my code ---------------------

        self.DialogModel.Title = "MainDialog"
        # mri(self.ctx, self.DialogContainer)

    def myFunction(self):
        # TODO: not implemented
        pass

    # --------- helpers ---------------------

    def messageBox(self, MsgText, MsgTitle, MsgType=MESSAGEBOX, MsgButtons=BUTTONS_OK):
        sm = self.ctx.ServiceManager
        si = sm.createInstanceWithContext("com.sun.star.awt.Toolkit", self.ctx)
        mBox = si.createMessageBox(self.Toolkit, MsgType, MsgButtons, MsgTitle, MsgText)
        mBox.execute()

    # -----------------------------------------------------------
    #               Execute dialog
    # -----------------------------------------------------------

    def showDialog(self):
        self.DialogContainer.setVisible(True)
        self.DialogContainer.createPeer(self.Toolkit, None)
        self.DialogContainer.execute()

    # -----------------------------------------------------------
    #               Action events
    # -----------------------------------------------------------
    def createButton_OnClick(self):
        createDialog = CreateDialog(ctx=self.ctx)
        createDialog.showDialog()

    def importButton_OnClick(self):
        importDialog = ImportDialog(ctx=self.ctx)
        importDialog.showDialog()

    def closeButton_OnClick(self):
        self.DialogModel.Title = "It's Alive! - closeButton"
        self.messageBox("It's Alive! - closeButton", "Event: OnClick", INFOBOX)
        # TODO: not implemented


# def Run_MainDialog(*args):
#
#     try:
#         ctx = remote_ctx                    # IDE
#     except:
#         ctx = uno.getComponentContext()     # UI
#
#     # get desktop
#     desktop = ctx.getByName("/singletons/com.sun.star.frame.theDesktop")
#
#     # get document
#     document = desktop.getCurrentComponent()
#
#     app = MainDialog(ctx=ctx)
#     app.showDialog()
#
#
# # Execute macro from LibreOffice UI (Tools - Macro)
# g_exportedScripts = Run_MainDialog,

