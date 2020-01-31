import os
from shutil import copyfile, copytree
import sys
import uno
import subprocess
import unohelper
import traceback

# Setup intro
def prepare_new_install(ctx):
    theme_name = "default-libreoffice"
    OK = True
    # get program install dir
    ps = ctx.getServiceManager().createInstanceWithContext('com.sun.star.util.PathSubstitution', ctx)
    instdir = uno.fileUrlToSystemPath(ps.getSubstituteVariableValue("$(instpath)"))
    program_sysdir = instdir + "/program"
    personas_sysdir = instdir + "/share/gallery/personas"
    sofficerc_file = "/sofficerc"

    # dir on macos
    if sys.platform.startswith("darwin"):
        program_sysdir = instdir + "/MacOS"
        personas_sysdir = instdir + "/Resources/gallery/personas"
    # dir on windows
    elif sys.platform.startswith("win"):
        sofficerc_file = "/soffice.ini"

    userdir = uno.fileUrlToSystemPath(ps.getSubstituteVariableValue("$(userurl)"))
    personas_userdir = userdir + "/gallery/personas"
    lotcdir = userdir + "/lotc-themes"

    prefered_themedir = "%s/%s" % (lotcdir, theme_name)

    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # when lotc-prepare is exists, it should not continue preparation setup in instdir
    if os.path.exists(userdir + "/lotc-prepare"):
        #TODO check version libreoffice inside lotc-prepare content
        return
         
    if not os.path.exists(personas_userdir):
        copytree(personas_sysdir, personas_userdir)

    if not os.path.exists(prefered_themedir):
        os.makedirs(prefered_themedir + "/program")
        os.makedirs(prefered_themedir + "/personas")
        copyfile(program_sysdir + "/intro.png", prefered_themedir + "/program/intro.png")
        copyfile(program_sysdir + sofficerc_file, prefered_themedir + "/program/sofficerc")


    if os.path.exists(lotcdir + "/active-theme"):
        os.remove(lotcdir + "/active-theme")

    # create symlink to active theme.
    # it will be live at (as symlink):
    # $HOME/.config/libreoffice/4/user/lotc/active-theme -> $HOME/.config/libreoffice/4/user/lotc/$THEME_NAME
    try:
        if sys.platform.startswith("win"):
            import ctypes
            # os.system("MKLINK /D {1} {0}".format(replace_separator(prefered_themedir), replace_separator(lotcdir+"/active-theme")))
            # os.symlink(replace_separator(prefered_themedir), replace_separator(lotcdir+"/active-theme"), True)
            if not ctypes.windll.shell32.IsUserAnAdmin():
                print('[!] The script is NOT running with administrative privileges')
                RUN_ME = "import os; os.symlink('{0}','{1}',True)"
                cmd = '{}'.format(RUN_ME.format(replace_separator(replace_separator(prefered_themedir),"/","\\\\"), replace_separator(replace_separator(lotcdir+"/active-theme"),"/","\\\\")))
                #os.symlink(replace_separator(prefered_themedir), replace_separator(lotcdir+"/active-theme"), True)
                try:
                    from ThemeChanger.Windows import elevate_commands
                    elevate_commands(cmd, "01.py")
                except Exception as e:
                    OK = False
                    print("Unable to complete new link active-theme, reason: " + str(e))
                    traceback.print_exc()
                    sys.exit(e.errno)
        else:
            os.symlink(prefered_themedir, lotcdir + "/active-theme")
    except Exception as e:
        OK = False
        print("Error on preparing active theme symlink")
        print(e)
        traceback.print_exc()
    active_dir = lotcdir + "/active-theme"
    RUN_ME = "import os, sys;" \
             "sys.path.append('{0}');" \
             "from Helper import setup_intro_image, setup_sofficerc, setup_personas;" \
             "setup_intro_image('{1}', '{2}');" \
             "setup_sofficerc('{1}', '{2}');" \
             "setup_personas('{3}', '{4}');"

    if sys.platform.startswith("win"):
        import ctypes
        # run in windows
        try:
            if not ctypes.windll.shell32.IsUserAnAdmin():
                print('[!] The script is NOT running with administrative privileges')
                cmd = '{}'.format(RUN_ME.format(replace_separator(current_dir),
                                                replace_separator(program_sysdir),
                                                replace_separator(active_dir),
                                                replace_separator(personas_sysdir),
                                                replace_separator(personas_userdir)))
                try:
                    from ThemeChanger.Windows import elevate_commands
                    elevate_commands(cmd, "02.py")
                except Exception as e:
                    OK = False
                    print("Unable to complete new installation, reason: " + str(e))
                    traceback.print_exc()
                    sys.exit(e.errno)
        except Exception as e:
            OK = False
            print(e)
            traceback.print_exc()
    else:
        # run as Administrator
        sudo = "sudo"
        if sys.platform.startswith("darwin"):
            try:
                # on macOS lauch libreoffice without splash banner
                setup_sofficerc(program_sysdir, active_dir)
                setup_personas(personas_sysdir, personas_userdir)
            except Exception as e:
                OK = False
                print(e)
                traceback.print_exc()

        elif sys.platform.startswith("linux"):
            if os.environ.get("FLATPAK_ID"):
                # flatpak
                insdir_flatpak = os.environ.get("HOME") + "/.local/share/flatpak/app/org.libreoffice.LibreOffice/x86_64/stable/active/files/libreoffice"
                progdir_flatpak = insdir_flatpak + "/program"
                personasdir_flatpak = insdir_flatpak + "/share/gallery/personas"
                setup_intro_image(progdir_flatpak, active_dir)
                setup_sofficerc(progdir_flatpak, active_dir)
                setup_personas(personasdir_flatpak, personas_userdir)
            elif os.environ.get("SNAP"):
                # snap
                # in snap install, you have to run lo_modify_snap.sh in your HOMEDIR via terminal
                copyfile(current_dir+"/../../lotc-modify-snap.sh", os.getenv("HOME")+"/lotc-modify-snap.sh")
                # preparing lo_modify_snap.sh content
                os.system("sed -i 's|REPLACEMOUNTPOINT|{}|' {}".format(os.getenv("SNAP"), os.getenv("HOME")+"/lotc-modify-snap.sh"))
                os.system("sed -i 's|REPLACEREV|{}|' {}".format(os.getenv("SNAP_REVISION"), os.getenv("HOME")+"/lotc-modify-snap.sh"))
                os.system("sed -i 's|REPLACEUSERDIR|{}|' {}".format(userdir, os.getenv("HOME")+"/lotc-modify-snap.sh"))
                os.system("sed -i 's|REPLACEINTRO|{}|' {}".format(active_dir + "/program/intro.png", os.getenv("HOME")+"/lotc-modify-snap.sh"))
                os.system("sed -i 's|REPLACESOFFICERC|{}|' {}".format(active_dir + "/program/sofficerc", os.getenv("HOME")+"/lotc-modify-snap.sh"))
                os.system("sed -i 's|REPLACEPERSONAS|{}|' {}".format(personas_userdir, os.getenv("HOME")+"/lotc-modify-snap.sh"))
                return "SNAP"
            else:
                # normal linux installation
                if os.environ.get("DISPLAY"):
                    prompts = ["pkexec","gksudo", "kdesudo"]
                    for item in prompts:
                        a = os.system("which %s" % item)
                        if a == 0:
                            sudo = item
                            break
                subprocess.call([sudo, sys.executable, "-c", RUN_ME.format(current_dir, program_sysdir, active_dir, personas_sysdir, personas_userdir)])
    # write config that preparation completed
    if OK:
        with open(userdir + "/lotc-prepare", "w") as f:
            #TODO write libreoffice installed version
            f.write("finished")
    return "OK"

def setup_intro_image(program_sysdir, prefered_themedir):
    # backup intro.png
    if not os.path.islink(program_sysdir + "/intro.png"):
        try:
            if sys.platform.startswith("win"):
                # rename
                os.rename(program_sysdir + "/intro.png", program_sysdir + "/intro.png.orig")
                # re-link
                # os.system("MKLINK {1} {0}".format(replace_separator(prefered_themedir + "/program/intro.png"), replace_separator(program_sysdir + "/intro.png")))
                os.symlink('{}'.format(replace_separator(prefered_themedir + "/program/intro.png","/","\\\\")), '{}'.format(replace_separator(program_sysdir + "/intro.png","/","\\\\")), False)
            else:
                os.rename(program_sysdir + "/intro.png", program_sysdir + "/intro.png.orig")
                os.symlink(prefered_themedir + "/program/intro.png", program_sysdir + "/intro.png")
            print("intro.png preparation success")
        except Exception as e:
            print("Error on preparing intro.png")
            print(e)
            traceback.print_exc()

def setup_sofficerc(program_sysdir, prefered_themedir):
    sofficerc = "/sofficerc"
    # on Windows sofficerc is soffice.ini
    if sys.platform.startswith("win"):
        sofficerc = "/soffice.ini"
    # setup sofficcerc
    if os.path.exists(program_sysdir + sofficerc):
        try:
            if sys.platform.startswith("win"):
                # rename
                os.rename(program_sysdir + sofficerc, program_sysdir + "/soffice.ini.orig")
                # re-link
                # os.system("MKLINK {1} {0}".format(replace_separator(prefered_themedir + "/sofficerc"), replace_separator(program_sysdir + sofficerc)))
                os.symlink('{}'.format(replace_separator(prefered_themedir + "/sofficerc","/","\\\\")), '{}'.format(replace_separator(program_sysdir + sofficerc,"/","\\\\")), False)
            else:
                os.rename(program_sysdir + sofficerc, program_sysdir + sofficerc + ".orig")
                os.symlink(prefered_themedir + "/program/sofficerc", program_sysdir + sofficerc)
            print("sofficerc preparation success")
        except Exception as e:
            print("Error on preparing sofficerc")
            print(e)
            traceback.print_exc()

def setup_personas(personas_sysdir, personas_userdir):
    # setup personas dir
    if os.path.exists(personas_sysdir) and not os.path.islink(personas_sysdir):
        try:
            if sys.platform.startswith("win"):
                # rename
                os.rename(personas_sysdir, personas_sysdir + ".orig")
                # re-link
                # os.system("MKLINK /D {1} {0}".format(replace_separator(personas_userdir), replace_separator(personas_sysdir)))
                os.symlink('{}'.format(replace_separator(personas_userdir,"/","\\\\")), '{}'.format(replace_separator(personas_sysdir,"/","\\\\")), True)
            else:
                os.rename(personas_sysdir, personas_sysdir + ".orig")
                os.symlink(personas_userdir, personas_sysdir)
            print("personas lists preparation success")
        except Exception as e:
            print("Error on preparing personas")
            print(e)
            traceback.print_exc()

def parse_manifest(manifest_dir):
    try:
        import xml.etree.ElementTree as Et
        root = Et.parse(manifest_dir+"/manifest.xml").getroot()
        theme_name = root.find("theme_name").text
        description = root.find("description").text
        version = root.find("version").text
        author = root.find("author").text
        author_link = root.find("author_url").text
        if root.find("icon_theme") != None:
            icon_theme = root.find("icon_theme").text
        else:
            icon_theme = "auto"
        # parsing custom_xcu
        if root.find("custom_xcu") != None:
            # get first index of XCU parent (oor:items)
            xcu_node = root.find("custom_xcu")[0]
            custom_xcu = []
            for item in xcu_node:
                current_item = {"path": item.attrib.get('{http://openoffice.org/2001/registry}path')}
                property_name = item.find('prop').attrib.get('{http://openoffice.org/2001/registry}name')
                current_item["property_name"] = property_name
                property_value = item.find('prop').find('value').text
                current_item["property_value"] = property_value
                custom_xcu.append(current_item)
        else:
            custom_xcu = []
        if sys.platform.startswith("win"):
            screenshots = ["file:///{}\\{}".format(replace_separator(manifest_dir,"/","\\"), replace_separator(ss.text,"/","\\")) for ss in root.findall("assets/img")]
        else:
            screenshots = ["file://{}/{}".format(manifest_dir, ss.text) for ss in root.findall("assets/img")]
        source_link = [{"text": sl.text, "url": sl.attrib["src"]} for sl in root.findall("source_link/link")]
        # persona_path = root.find("assets/persona_list").text
        data = {
            "author": author,
            "author_url": author_link,
            "description": description,
            "name": theme_name,
            "screenshots": screenshots,
            "version": version,
            "source_link": source_link,
            "icon_theme": icon_theme,
            "custom_xcu" : custom_xcu
        }
        # print(data)
        return data
    except FileNotFoundError:
        return None

def get_user_dir(ctx):
    ps = ctx.getServiceManager().createInstanceWithContext('com.sun.star.util.PathSubstitution', ctx)
    userdir = uno.fileUrlToSystemPath(ps.getSubstituteVariableValue("$(userurl)"))
    return userdir

def get_tmp_dir():
    import tempfile
    return tempfile.gettempdir()

# Adopted from MRi Extension
# read config value from the node and the property name
def get_configvalue(ctx, nodepath, prop):
    from com.sun.star.beans import PropertyValue
    cp = ctx.getServiceManager().createInstanceWithContext(
        'com.sun.star.configuration.ConfigurationProvider', ctx)
    node = PropertyValue()
    node.Name = 'nodepath'
    node.Value = nodepath
    try:
        cr = cp.createInstanceWithArguments(
            'com.sun.star.configuration.ConfigurationAccess', (node,))
        if cr and (cr.hasByName(prop)):
            return cr.getPropertyValue(prop)
    except:
        return None

def replace_separator(text, what="\\", withs="/"):
    return text.replace(what,withs)