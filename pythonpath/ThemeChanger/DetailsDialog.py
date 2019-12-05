# -*- coding: utf-8 -*-
#!/usr/bin/env python

import uno
from com.sun.star.awt.MessageBoxButtons import BUTTONS_OK, BUTTONS_OK_CANCEL, BUTTONS_YES_NO, BUTTONS_YES_NO_CANCEL, BUTTONS_RETRY_CANCEL, BUTTONS_ABORT_IGNORE_RETRY
from com.sun.star.awt.MessageBoxButtons import DEFAULT_BUTTON_OK, DEFAULT_BUTTON_CANCEL, DEFAULT_BUTTON_RETRY, DEFAULT_BUTTON_YES, DEFAULT_BUTTON_NO, DEFAULT_BUTTON_IGNORE
from com.sun.star.awt.MessageBoxType import MESSAGEBOX, INFOBOX, WARNINGBOX, ERRORBOX, QUERYBOX
from ThemeChanger.UI.DetailsDialog_UI import DetailsDialog_UI
from ThemeChanger.Helper import get_user_dir, get_configvalue, replace_separator
import traceback
import sys
if sys.platform.startswith("win"):
    from ThemeChanger.Windows import elevate_commands

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
        if self.theme_data["name"] == "Default LibreOffice":
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
                os.remove(replace_separator(active_theme))
                if sys.platform.startswith("win"):
                    cmd = "import os; os.symlink('{0}','{1}',True)".format(
                        replace_separator(replace_separator(default_theme_path),"/","\\\\"),
                        replace_separator(replace_separator(active_theme),"/","\\\\"))
                    try:
                        elevate_commands(cmd,"relinkdefaulttheme.py")
                    except Exception as e:
                        self.messageBox("Unable to complete re-link active-theme, reason: "+str(e), "Error Linking to Default Theme", ERRORBOX)
                        traceback.print_exc()
                        sys.exit(1)
                else:
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
                        fout.writelines(current_personas_data[1:]+"\n")
                    self.update_registry(None)
                    self.messageBox("Success removing theme", "Remove Theme", INFOBOX)
                    self.DialogContainer.getControl("RemoveButton").setEnable(False)
                    self.DialogContainer.getControl("InstallButton").setEnable(False)
                except Exception as e:
                    print(e)
                    traceback.print_exc()

    def InstallButton_OnClick(self):
        try:
            import os
            import sys
            personas_userdir = get_user_dir(self.ctx) + "/gallery/personas"
            theme_location = self.theme_data["theme_location"]
            active_theme = get_user_dir(self.ctx) + "/lotc-themes/active-theme"
            # print(os.path.basename(theme_location))
            # re-link active-theme
            if theme_location != os.readlink(active_theme):
                os.remove(replace_separator(active_theme))
                if sys.platform.startswith("win"):
                    cmd = "import os; os.symlink('{0}','{1}',True)".format(
                        replace_separator(replace_separator(theme_location),"/","\\\\"),
                        replace_separator(replace_separator(active_theme),"/","\\\\"))
                    try:
                        elevate_commands(cmd,"relinktheme.py")
                    except Exception as e:
                        print("Unable to complete re-link active-theme, reason: "+str(e))
                        traceback.print_exc()
                        os.rename(replace_separator(active_theme+".orig"),replace_separator(active_theme))
                else:
                    os.symlink(theme_location, active_theme)
            # copy personas to user gallery
            current_personas_data = None
            if not self.theme_data["name"] == "Default LibreOffice":
                for item in os.listdir(active_theme + "/personas/"):
                    if os.path.isdir(active_theme + "/personas/" + item):
                        personas = item
                if not os.path.exists(personas_userdir + "/" + personas):
                    import shutil
                    # copy dir
                    shutil.copytree(active_theme + "/personas/" + personas, personas_userdir + "/" + personas)
                # append personas data to top of system personas_list.txt
                with open(active_theme + "/personas/personas_list.txt") as file:
                    current_personas_data = file.read()
                with open(personas_userdir + "/personas_list.txt","r+") as file:
                    current_content = file.read()
                    file.seek(0,0)
                    if current_personas_data not in current_content:
                        file.write(current_personas_data + current_content + "\n")
            # update the registry
            self.update_registry(current_personas_data)
            self.current_active_theme = self.theme_data["name"]
            self.messageBox("{} was successfully installed, relaunch LibreOffice to apply changes".format(self.theme_data["name"]), "Success!",INFOBOX)
            self.DialogContainer.getControl("RemoveButton").setLabel("Deactivate")
            self.DialogContainer.getControl("InstallButton").setEnable(False)
            self.DialogContainer.getControl("InstallButton").setLabel("Activated")
        except Exception as e:
            print(e)
            traceback.print_exc()

    def update_registry(self, personas_data):
        try:
            # /org.openoffice.Office.Common/Misc
            # nodepath = "/org.openoffice.Office.Common/Misc"
            if personas_data == None:
                persona= "no"
                persona_settings = ""
            else:
                persona = "default"
                persona_settings = personas_data.strip()
            self.write_config(persona,persona_settings)

        except Exception as e:
            print(e)
            traceback.print_exc()
            exit(-1)

    def write_config(self, persona_data, personasettings_data):
        from com.sun.star.beans import PropertyValue
        config_provider = self.ctx.getServiceManager().createInstanceWithContext(
            'com.sun.star.configuration.ConfigurationProvider', self.ctx)
        node = PropertyValue()
        node.Name = 'nodepath'
        node.Value = "/org.openoffice.Office.Common/Misc"
        try:
            config_writer = config_provider.createInstanceWithArguments(
                'com.sun.star.configuration.ConfigurationUpdateAccess', (node,))
            cfg_names = ("Persona", "PersonaSettings")
            cfg_values = (persona_data, personasettings_data)
            config_writer.setPropertyValues(cfg_names, cfg_values)

            config_writer.commitChanges()
        except:
            raise
