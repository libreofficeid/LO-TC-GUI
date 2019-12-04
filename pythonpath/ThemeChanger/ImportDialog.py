# -*- coding: utf-8 -*-
#!/usr/bin/env python

import uno
from com.sun.star.awt.MessageBoxButtons import BUTTONS_OK, BUTTONS_OK_CANCEL, BUTTONS_YES_NO, BUTTONS_YES_NO_CANCEL, BUTTONS_RETRY_CANCEL, BUTTONS_ABORT_IGNORE_RETRY
from com.sun.star.awt.MessageBoxButtons import DEFAULT_BUTTON_OK, DEFAULT_BUTTON_CANCEL, DEFAULT_BUTTON_RETRY, DEFAULT_BUTTON_YES, DEFAULT_BUTTON_NO, DEFAULT_BUTTON_IGNORE
from com.sun.star.awt.MessageBoxType import MESSAGEBOX, INFOBOX, WARNINGBOX, ERRORBOX, QUERYBOX
from ThemeChanger.UI.ImportDialog_UI import ImportDialog_UI


# -------------------------------------
# HELPERS FOR MRI AND  XRAY
# -------------------------------------

# Uncomment for MRI
def mri(ctx, target):
    mri = ctx.ServiceManager.createInstanceWithContext("mytools.Mri", ctx)
    mri.inspect(target)

class ImportDialog(ImportDialog_UI):
    '''
    Class documentation...
    '''
    def __init__(self, ctx=uno.getComponentContext(), **kwargs):
        self.ctx = ctx
        ImportDialog_UI.__init__(self, self.ctx)

        # --------- my code ---------------------

        self.DialogModel.Title = "ImportDialog"
        # mri(self.ctx, self.DialogContainer)

    # --------- helpers ---------------------

    def messageBox(self, MsgText, MsgTitle, MsgType=MESSAGEBOX, MsgButtons=BUTTONS_OK):
        sm = self.ctx.ServiceManager
        si = sm.createInstanceWithContext("com.sun.star.awt.Toolkit", self.ctx)
        mBox = si.createMessageBox(self.Toolkit, MsgType, MsgButtons, MsgTitle, MsgText)
        mBox.execute()

    # -----------------------------------------------------------
    #               Execute dialog
    # -----------------------------------------------------------

    def pick_lotc(self):
        try:
            sm = self.ctx.ServiceManager
            filepicker = sm.createInstanceWithContext("com.sun.star.ui.dialogs.FilePicker", self.ctx)
            filepicker.setMultiSelectionMode(False)
            filepicker.appendFilter("LibreOffice Theme (*.lotc)","*.lotc")
            filepicker.setTitle("Select lotc file")
            if filepicker.execute():
                print(filepicker.getFiles())
                import sys
                if sys.platform.startswith("win"):
                    self.DialogContainer.getControl("LotcLocation").Text = filepicker.getFiles()[0][8:]
                else:
                    self.DialogContainer.getControl("LotcLocation").Text = filepicker.getFiles()[0][7:]
        except Exception as e:
            import traceback
            traceback.print_exc()

    def get_lotc_location(self):
        lotc_location = self.DialogContainer.getControl("LotcLocation").getText()
        extension = lotc_location[-5:].lower()
        if extension != ".lotc" or lotc_location == "" or lotc_location == None:
            lotc_location = None
        return lotc_location

    def showDialog(self):
        self.DialogContainer.setVisible(True)
        self.DialogContainer.createPeer(self.Toolkit, None)
        if self.DialogContainer.execute() == 1:
            theme_location = self.get_lotc_location()
            if not theme_location == None:
                return theme_location
            else:
                self.messageBox("Oops, your selected theme is not lotc file","Error",MsgType=ERRORBOX)
                self.showDialog()
        else:
            return None