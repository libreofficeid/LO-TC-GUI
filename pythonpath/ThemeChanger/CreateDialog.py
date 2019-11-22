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
            try:
                import xml.etree.cElementTree as Et
                root = Et.Element("lotc")
                Et.SubElement(root, "theme_name").text = data["name"]
                Et.SubElement(root, "version").text = data["version"]
                Et.SubElement(root, "author").text = data["author"]
                Et.SubElement(root, "author_url").text = "https://mywebsite.com"
                Et.SubElement(root, "description").text = "this is my libreoffice theme description"
                personas = Et.SubElement(root, "assets", {"id": "personas"})
                Et.SubElement(personas, "persona_list").text = "personas/personas_list.txt"
                Et.SubElement(personas, "footer_img").text = "personas/{}/footer.png".format(data["name"].title().replace(" ",""))
                Et.SubElement(personas, "header_img").text = "personas/{}/header.png".format(data["name"].title().replace(" ",""))
                Et.SubElement(personas, "preview").text = "personas/{}/preview.png".format(data["name"].title().replace(" ",""))
                program = Et.SubElement(root,"assets", {"id": "program"})
                Et.SubElement(program, "intro").text = "program/intro.png"
                Et.SubElement(program, "soffice").text = "program/sofficerc"
                screenshots = Et.SubElement(root, "assets", {"id": "screenshots"})
                Et.SubElement(screenshots, "img", {"id": "screenshot-1"}).text = "screenshots/screenshot-1.png"
                Et.SubElement(screenshots, "img", {"id": "screenshot-2"}).text = "screenshots/screenshot-2.png"
                source_link = Et.SubElement(root, "source_link")
                Et.SubElement(source_link, "link", {"id": "1", "src": "https://source-link-1"}).text = "About {}".format(data["name"])
                Et.SubElement(source_link, "link", {"id": "2", "src": "https://source-link-2"}).text = "License"
                # write to file
                tree = Et.ElementTree(root)
                self.indent(root)
                tree.write(save_to,encoding="UTF-8",xml_declaration=True,method="xml")
            except Exception as e:
                print(e)
                import traceback
                traceback.print_exc()
        # personas file
        if content_type == "personas":
            text_personas = "{0};{0};{0}/preview.png;{0}/header.png;{0}/footer.png;#ffffff;#000000".format(data["name"].title().replace(" ",""))
            try:
                with open(save_to, "w") as file:
                    file.write(text_personas)
            except Exception as e:
                print(e)
                import traceback
                traceback.print_exc()

    def create_new_theme(self, theme_name, author_name, new_location_path):
        # make requiered directories
        makedirs(new_location_path+"/program")
        makedirs(new_location_path + "/personas/" + theme_name.title().replace(" ",""))
        makedirs(new_location_path + "/screenshots")
        # write sample manifest to theme path
        theme_manifest_path = new_location_path + "/manifest.xml"
        theme_manifest_data = {"name": theme_name, "author": author_name, "version": "1.0"}
        self.write_content(content_type="xml", save_to=theme_manifest_path, data=theme_manifest_data)
        # write sample personas_list to theme path
        personas_path = new_location_path + "/personas/personas_list.txt"
        self.write_content(content_type="personas", save_to=personas_path, data=theme_manifest_data)

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

    def indent(self, elem, level=0):
        i = "\n" + level * "  "
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "  "
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for elem in elem:
                self.indent(elem, level + 1)
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i


    # -----------------------------------------------------------
    #               Execute dialog
    # -----------------------------------------------------------

    def showDialog(self):
        self.DialogContainer.setVisible(True)
        self.DialogContainer.createPeer(self.Toolkit, None)
        if self.DialogContainer.execute() == 1:
            theme_name = self.get_theme_name()
            new_theme_path = theme_name.replace(" ","-").lower()
            new_location_path = self.get_new_theme_location() + "/" + new_theme_path
            author_name = self.get_author_name()
            if theme_name == "" or author_name == "" or new_location_path == "":
                self.messageBox("Please fill all fields","Empty Field", MsgType=ERRORBOX)
                self.showDialog()
                return
            else:
                if not exists(new_location_path):
                    try:
                        makedirs(new_location_path)
                    except OSError as e:
                        import traceback
                        print(e)
                        self.messageBox("Unable to create destination path %s.\n%s" % (new_location_path, traceback.print_exc()),"Error",MsgType=ERRORBOX)
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
