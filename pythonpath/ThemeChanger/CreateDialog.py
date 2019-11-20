# -*- coding: utf-8 -*-
#!/usr/bin/env python

import uno
from com.sun.star.awt.MessageBoxButtons import BUTTONS_OK, BUTTONS_OK_CANCEL, BUTTONS_YES_NO, BUTTONS_YES_NO_CANCEL, BUTTONS_RETRY_CANCEL, BUTTONS_ABORT_IGNORE_RETRY
from com.sun.star.awt.MessageBoxButtons import DEFAULT_BUTTON_OK, DEFAULT_BUTTON_CANCEL, DEFAULT_BUTTON_RETRY, DEFAULT_BUTTON_YES, DEFAULT_BUTTON_NO, DEFAULT_BUTTON_IGNORE
from com.sun.star.awt.MessageBoxType import MESSAGEBOX, INFOBOX, WARNINGBOX, ERRORBOX, QUERYBOX
from ThemeChanger.UI.CreateDialog_UI import CreateDialog_UI

from os import makedirs
from os.path import exists

# -------------------------------------
# HELPERS FOR MRI AND  XRAY
# -------------------------------------

# Uncomment for MRI
def mri(ctx, target):
    mri = ctx.ServiceManager.createInstanceWithContext("mytools.Mri", ctx)
    mri.inspect(target)

class CreateDialog(CreateDialog_UI):
    '''
    Class documentation...
    '''
    def __init__(self, ctx=uno.getComponentContext(), **kwargs):

        self.ctx = ctx
        CreateDialog_UI.__init__(self, self.ctx)

        # --------- my code ---------------------

        self.DialogModel.Title = "CreateDialog"
        # mri(self.ctx, self.DialogModel)

    def get_theme_name(self):
        return self.DialogContainer.getControl("ThemeNameField").Text

    def get_new_theme_location(self):
        return self.DialogContainer.getControl("NewThemeFolderField").Text

    def get_author_name(self):
        return self.DialogContainer.getControl("AuthorNameField").Text

    def write_content(self, content_type="xml", save_to="", data={}):
        # xml
        if content_type == "xml":
            import xml.etree.cElementTree as Et
            root = Et.Element("lotc_theme")
            Et.SubElement(root, "name").text = data["name"]
            Et.SubElement(root, "version").text = data["version"]
            Et.SubElement(root, "author").text = data["author"]
            Et.SubElement(root, "description").text = "this is my libreoffice theme description"
            # write to file
            tree = Et.ElementTree(root)
            tree.write(save_to,encoding="UTF-8",xml_declaration=True,method="xml")

    def create_new_theme(self, theme_name, author_name, new_location_path):
        # make requiered directories
        makedirs(new_location_path+"/program")
        makedirs(new_location_path + "/share/gallery/personas/" + theme_name)
        # write sample manifest to theme path
        theme_manifest_path = new_location_path + "/manifest.xml"
        theme_manifest_data = {"name": theme_name, "author": author_name, "version": "1.0"}
        self.write_content(content_type="xml", save_to=theme_manifest_path, data=theme_manifest_data)

        return self.messageBox("Successfully initializing your new theme in: %s\n \n A complete guide to create LO-TC themes can be found at: https://libreoffice.id/lotc" % new_location_path,"Success!")
        pass

    # --------- helpers ---------------------

    def messageBox(self, MsgText, MsgTitle, MsgType=MESSAGEBOX, MsgButtons=BUTTONS_OK):
        sm = self.ctx.ServiceManager
        si = sm.createInstanceWithContext("com.sun.star.awt.Toolkit", self.ctx)
        mBox = si.createMessageBox(self.Toolkit, MsgType, MsgButtons, MsgTitle, MsgText)
        mBox.execute()

    def pick_folder(self):
        try:
            sm = self.ctx.ServiceManager
            filepicker = sm.createInstanceWithContext("com.sun.star.ui.dialogs.FolderPicker", self.ctx)
            filepicker.setTitle("Select folder to save theme")
            if filepicker.execute():
                self.DialogContainer.getControl("NewThemeFolderField").Text = filepicker.getDirectory()[7:]
        except Exception as e:
            import traceback
            traceback.print_exc()


    # -----------------------------------------------------------
    #               Execute dialog
    # -----------------------------------------------------------

    def showDialog(self):
        self.DialogContainer.setVisible(True)
        self.DialogContainer.createPeer(self.Toolkit, None)
        if self.DialogContainer.execute() == 1:
            theme_name = self.get_theme_name()
            new_location_path = self.get_new_theme_location() + "/" + theme_name
            author_name = self.get_author_name()
            if theme_name == "" or author_name == "" or new_location_path == "":
                self.messageBox("Please fill all fields","Empty Field")
                self.showDialog()
                return
            else:
                if not exists(new_location_path):
                    try:
                        makedirs(new_location_path)
                    except OSError as e:
                        import traceback
                        print(e)
                        self.messageBox("Unable to create destination path %s.\n%s" % (new_location_path, traceback.print_exc()),"Error")
                        self.showDialog()

                return self.create_new_theme(theme_name, author_name, new_location_path)
        else:
            return None

    # -----------------------------------------------------------
    #               Action events
    # -----------------------------------------------------------

    # def CommandButton1_OnClick(self):
    #     self.DialogModel.Title = "It's Alive! - CommandButton1"
    #     self.messageBox("It's Alive! - CommandButton1", "Event: OnClick", INFOBOX)
    #     # TODO: not implemented
    #
    # def CommandButton2_OnClick(self):
    #     self.DialogModel.Title = "It's Alive! - CommandButton2"
    #     self.messageBox("It's Alive! - CommandButton2", "Event: OnClick", INFOBOX)
    #     # TODO: not implemented
