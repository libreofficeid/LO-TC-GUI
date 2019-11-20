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
    # get program install dir
    ps = ctx.getServiceManager().createInstanceWithContext('com.sun.star.util.PathSubstitution', ctx)
    instdir = uno.fileUrlToSystemPath(ps.getSubstituteVariableValue("$(instpath)"))
    program_sysdir = instdir + "/program"
    personas_sysdir = instdir + "/share/gallery/personas"

    userdir = uno.fileUrlToSystemPath(ps.getSubstituteVariableValue("$(userurl)"))
    personas_userdir = userdir + "/gallery/personas"
    lotcdir = userdir + "/lotc-themes"

    prefered_themedir = "%s/%s" % (lotcdir, theme_name)

    current_dir = os.path.dirname(os.path.abspath(__file__))

    if os.path.exists(userdir + "/lotc-prepare"):
        return

    if not os.path.exists(personas_userdir):
        copytree(personas_sysdir, personas_userdir)

    if not os.path.exists(prefered_themedir):
        os.makedirs(prefered_themedir + "/program")
        os.makedirs(prefered_themedir + "/personas")
        copyfile(program_sysdir + "/intro.png", prefered_themedir + "/program/intro.png")
        copyfile(program_sysdir + "/sofficerc", prefered_themedir + "/program/sofficerc")


    if os.path.exists(lotcdir + "/active-theme"):
        os.remove(lotcdir + "/active-theme")

    # create symlink to active theme.
    # it will be live at (as symlink):
    # $HOME/.config/libreoffice/4/user/lotc/active-theme -> $HOME/.config/libreoffice/4/user/lotc/$THEME_NAME
    try:
        os.symlink(prefered_themedir, lotcdir + "/active-theme")
    except Exception as e:
        print(e)
        traceback.print_exc()
    active_dir = lotcdir + "/active-theme"
    RUN_ME = "import os, sys; " \
             "os.chdir('{}');" \
             "from Helper import setup_intro_image, setup_sofficerc, setup_personas;" \
             "setup_intro_image('{}', '{}');" \
             "setup_sofficerc('{}', '{}');" \
             "setup_personas('{}', '{}');".format(current_dir, program_sysdir, active_dir, program_sysdir, active_dir,
                                                  personas_sysdir, personas_userdir)

    if sys.platform.startswith("win"):
        pass
    else:
        # run as Administrator
        sudo = "sudo"
        if sys.platform.startswith("darwin"):
            sudo = "osascript"
            subprocess.call(["sudo", sudo, "python3", "-c", RUN_ME] + sys.argv)

        if sys.platform.startswith("linux"):
            if os.environ.get("DISPLAY"):
                prompts = ["pkexec","gksudo", "kdesudo"]
                for item in prompts:
                    a = os.system("which %s" % item)
                    if a == 0:
                        sudo = item
                        break
            subprocess.call([sudo, sys.executable, "-c", RUN_ME] + sys.argv)
        pass
    # write config that preparation completed
    with open(userdir + "/lotc-prepare", "w") as f:
        f.write("finished")
        f.close()
    return


def setup_intro_image(program_sysdir, prefered_themedir):
    # backup intro.png
    if not os.path.islink(program_sysdir + "/intro.png"):
        try:
            os.rename(program_sysdir + "/intro.png", program_sysdir + "/intro.png.orig")
            os.symlink(prefered_themedir + "/program/intro.png", program_sysdir + "/intro.png")
            print("intro.png preparation success")
        except Exception as e:
            print(e)
            traceback.print_exc()

def setup_sofficerc(program_sysdir, prefered_themedir):
    # setup sofficcerc
    if os.path.exists(program_sysdir + "/sofficerc"):
        try:
            os.rename(program_sysdir + "/sofficerc", program_sysdir + "/sofficerc.orig")
            os.symlink(prefered_themedir + "/program/sofficerc", program_sysdir + "/sofficerc")
            print("sofficerc preparation success")
        except Exception as e:
            print(e)
            traceback.print_exc()

def setup_personas(personas_sysdir, personas_userdir):
    # setup personas dir
    if os.path.exists(personas_sysdir) and not os.path.islink(personas_sysdir):
        try:
            os.rename(personas_sysdir, personas_sysdir + ".orig")
            os.symlink(personas_userdir, personas_sysdir)
            print("personas lists preparation success")
        except Exception as e:
            print(e)
            traceback.print_exc()

def parse_manifest(manifest_dir):
    if manifest_dir:
        import xml.etree.ElementTree as Et
        root = Et.parse(manifest_dir+"/manifest.xml").getroot()
        theme_name = root.find("theme_name").text
        description = root.find("description").text
        version = root.find("version").text
        author = root.find("author").text
        screenshots = ["file://{}/{}".format(manifest_dir, ss.text) for ss in root.findall("assets/img")]
        data = {
            "author": author,
            "description": description,
            "name": theme_name,
            "screenshots": screenshots,
            "version": version
        }
        # print(data)
        return data
    else:
        return None