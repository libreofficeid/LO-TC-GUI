# -*- coding: utf-8 -*-
#!/usr/bin/env python

import uno
from com.sun.star.awt.MessageBoxButtons import BUTTONS_OK, BUTTONS_OK_CANCEL, BUTTONS_YES_NO, BUTTONS_YES_NO_CANCEL, BUTTONS_RETRY_CANCEL, BUTTONS_ABORT_IGNORE_RETRY
from com.sun.star.awt.MessageBoxButtons import DEFAULT_BUTTON_OK, DEFAULT_BUTTON_CANCEL, DEFAULT_BUTTON_RETRY, DEFAULT_BUTTON_YES, DEFAULT_BUTTON_NO, DEFAULT_BUTTON_IGNORE
from com.sun.star.awt.MessageBoxType import MESSAGEBOX, INFOBOX, WARNINGBOX, ERRORBOX, QUERYBOX
from ThemeChanger.UI.DetailsDialog_UI import DetailsDialog_UI
from ThemeChanger.Helper import get_user_dir

# -------------------------------------
# HELPERS FOR MRI AND  XRAY
# -------------------------------------

# Uncomment for MRI
def mri(ctx, target):
    mri = ctx.ServiceManager.createInstanceWithContext("mytools.Mri", ctx)
    mri.inspect(target)

class DetailsDialog(DetailsDialog_UI):
    '''
    Class documentation...
    '''
    def __init__(self, ctx=uno.getComponentContext(), theme_data={}, **kwargs):
        self.theme_data = theme_data
        self.current_active_theme = theme_data["current_active"]
        self.ctx = ctx
        DetailsDialog_UI.__init__(self, self.ctx, self.theme_data)


        # --------- my code ---------------------

        # self.DialogModel.Title = "DetailsDialog"
        # mri(self.ctx, self.DialogContainer)

    # --------- helpers ---------------------

    def messageBox(self, MsgText, MsgTitle, MsgType=MESSAGEBOX, MsgButtons=BUTTONS_OK):
        sm = self.ctx.ServiceManager
        si = sm.createInstanceWithContext("com.sun.star.awt.Toolkit", self.ctx)
        mBox = si.createMessageBox(self.Toolkit, MsgType, MsgButtons, MsgTitle, MsgText)
        return mBox.execute()

    # -----------------------------------------------------------
    #               Execute dialog
    # -----------------------------------------------------------

    def showDialog(self):
        self.DialogContainer.setVisible(True)
        self.DialogContainer.createPeer(self.Toolkit, None)
        if self.theme_data["name"] == "default-libreoffice":
            self.DialogContainer.getControl("RemoveButton").setVisible(False)
        if self.theme_data["name"] == self.theme_data["current_active"]:
            self.DialogContainer.getControl("RemoveButton").setLabel("Deactivate")
            self.DialogContainer.getControl("InstallButton").setEnable(False)
            self.DialogContainer.getControl("InstallButton").setLabel("Activated")
        self.DialogContainer.execute()
        return self.current_active_theme

    # -----------------------------------------------------------
    #               Action events
    # -----------------------------------------------------------

    def RemoveButton_OnClick(self):
        import os
        # deactivate and return to default-libreoffice
        if self.DialogModel.getByName("RemoveButton").Label == "Deactivate":
            try:
                self.messageBox("Your theme will be deactivated", "Deactivate", INFOBOX)
                active_theme = get_user_dir(self.ctx) + "/lotc-themes/active-theme"
                default_theme_path = get_user_dir(self.ctx) + "/lotc-themes/default-libreoffice"
                os.remove(active_theme)
                os.symlink(default_theme_path, active_theme)
                self.update_registry(None)
                self.messageBox("Theme deactivation success!\nRelaunch LibreOffice to apply changes", "Deactivate", INFOBOX)
                self.DialogContainer.getControl("RemoveButton").setLabel("Remove")
                self.DialogContainer.getControl("InstallButton").setEnable(True)
                self.DialogContainer.getControl("InstallButton").setLabel("Activate")
                self.current_active_theme = "default-libreoffice"
                # os.system("killall soffice.bin")
            except Exception as e:
                print(e)
                import traceback
                traceback.print_exc()
        # prompt it will be removed permanently
        elif self.DialogModel.getByName("RemoveButton").Label == "Remove":
            choice = self.messageBox("This action will remove your theme, continue?",
                                     "Confirm Theme Removal", QUERYBOX, BUTTONS_YES_NO)
            # yes
            if choice == 2:
                try:
                    personas_userdir = get_user_dir(self.ctx) + "/gallery/personas"
                    theme_location = self.theme_data["theme_location"]
                    import shutil
                    # remove theme dir
                    if os.path.exists(theme_location):
                        shutil.rmtree(theme_location)
                    # remove personas dir
                    if os.path.exists(personas_userdir + "/" + os.path.basename(theme_location)):
                        shutil.rmtree(personas_userdir + "/" + os.path.basename(theme_location))
                    # update personas file
                    with open(personas_userdir + "/personas_list.txt", "r") as fin:
                        current_personas_data = fin.read().splitlines(True)
                    with open(personas_userdir + "/personas_list.txt", "w") as fout:
                        fout.writelines(current_personas_data[1:])
                    self.update_registry(None)
                    self.messageBox("Success removing theme", "Remove Theme", INFOBOX)
                    self.DialogContainer.getControl("RemoveButton").setEnable(False)
                    self.DialogContainer.getControl("InstallButton").setEnable(False)
                except Exception as e:
                    import traceback
                    print(e)
                    traceback.print_exc()

    def InstallButton_OnClick(self):
        try:
            import os
            personas_userdir = get_user_dir(self.ctx) + "/gallery/personas"
            theme_location = self.theme_data["theme_location"]
            active_theme = get_user_dir(self.ctx) + "/lotc-themes/active-theme"
            # print(os.path.basename(theme_location))
            # re-link active-theme
            if theme_location != os.readlink(active_theme):
                os.remove(active_theme)
                os.symlink(theme_location, active_theme)
            # copy personas to user gallery
            current_personas_data = None
            if not self.theme_data["name"] == "default-libreoffice":
                if not os.path.exists(personas_userdir + "/" + os.path.basename(theme_location)):
                    import shutil
                    # copy dir
                    shutil.copytree(active_theme + "/personas/" + os.path.basename(theme_location), personas_userdir + "/" + os.path.basename(theme_location))
                # append personas data to top of system personas_list.txt
                with open(active_theme + "/personas/personas_list.txt") as file:
                    current_personas_data = file.read()
                with open(personas_userdir + "/personas_list.txt","r+") as file:
                    current_content = file.read()
                    file.seek(0,0)
                    if current_personas_data not in current_content:
                        file.write(current_personas_data + current_content)
            # update the registry
            self.update_registry(current_personas_data)
            self.current_active_theme = self.theme_data["name"]
            self.messageBox("{} was successfully installed, relaunch LibreOffice to apply changes".format(self.theme_data["name"]), "Success!",INFOBOX)
            self.DialogContainer.getControl("RemoveButton").setLabel("Deactivate")
            self.DialogContainer.getControl("InstallButton").setEnable(False)
            self.DialogContainer.getControl("InstallButton").setLabel("Activated")
            # os.system("killall soffice.bin")
        except Exception as e:
            print(e)
            import traceback
            traceback.print_exc()

    def update_registry(self, personas_data):
        try:
            import xml.etree.ElementTree as ET
            registry_file = get_user_dir(self.ctx) + "/registrymodifications.xcu"
            ET.register_namespace("oor", "http://openoffice.org/2001/registry")
            ET.register_namespace("xs", "http://www.w3.org/2001/XMLSchema")
            ET.register_namespace("xsi", "http://www.w3.org/2001/XMLSchema-instance")
            root = ET.parse(registry_file).getroot()
            persona = root.find(".//*[@{http://openoffice.org/2001/registry}name='Persona']/value")
            persona_settings = root.find(".//*[@{http://openoffice.org/2001/registry}name='PersonaSettings']/value")
            if personas_data == None:
                persona.text = "no"
                persona_settings.text = ""
            else:
                persona.text = "default"
                persona_settings.text = personas_data.strip()
            tree = ET.ElementTree(root)
            tree.write(registry_file,encoding="UTF-8",xml_declaration=True,method="xml")
        except Exception as e:
            print(e)
            import traceback
            traceback.print_exc()
            exit(-1)