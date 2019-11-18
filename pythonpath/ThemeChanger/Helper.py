import os
from shutil import copyfile
import sys
import uno
import unohelper
import traceback

# Setup intro
def prepare_new_install(ctx, theme_name="default-libreoffice"):
    if sys.platform == "linux":

        pass
    elif sys.platform == "windows":
        pass
    else:
        pass
    return
    # get program install dir
    ps = ctx.getServiceManager().createInstanceWithContext('com.sun.star.util.PathSubstitution', ctx)
    instdir = uno.fileUrlToSystemPath(ps.getSubstituteVariableValue("$(instpath)"))
    program_sysdir = instdir + "/program"
    personas_sysdir = instdir + "/share/gallery/personas"

    userdir = uno.fileUrlToSystemPath(ps.getSubstituteVariableValue("$(userurl)"))
    personas_userdir = userdir + "/gallery/personas"
    lotcdir = userdir + "/lotc-themes"

    prefered_themedir = "%s/%s" % (lotcdir, theme_name)

    if os.path.exists(userdir + "/lotc-prepare"):
        return

    if not os.path.exists(prefered_themedir):
        os.makedirs(prefered_themedir)
        copyfile(program_sysdir + "/intro.png", prefered_themedir + "/intro.png")
        copyfile(program_sysdir + "/sofficerc", prefered_themedir + "/sofficerc")


    if os.path.exists(lotcdir + "/active-theme"):
        os.remove(lotcdir + "/active-themes")

    # create symlink to active theme.
    # it will be live at (as symlink):
    # $HOME/.config/libreoffice/4/user/lotc/active-theme -> $HOME/.config/libreoffice/4/user/lotc/$THEME_NAME
    try:
        os.symlink(prefered_themedir, lotcdir + "/active-theme")
    except Exception as e:
        print(e)
        traceback.print_exc()

    # backup intro.png
    # TODO check user privilege (because using root privileges to do this section)
    if not os.path.islink(program_sysdir + "/intro.png"):
        try:
            os.rename(program_sysdir + "/intro.png", program_sysdir + "/intro.png.orig")
            os.symlink(prefered_themedir, program_sysdir + "/intro.png")
        except Exception as e:
            print(e)
            traceback.print_exc()

    # setup sofficcerc
    # TODO check user privilege (because using root privileges to do below section)
    if os.path.exists(program_sysdir + "/sofficerc"):
        try:
            os.rename(program_sysdir + "/sofficerc", program_sysdir + "/sofficerc.orig")
            os.symlink(prefered_themedir, program_sysdir + "/sofficerc")
        except Exception as e:
            print(e)
            traceback.print_exc()


    # setup personas dir
    # TODO check user privilege (because using root privileges to do below section)
    if os.path.exists(personas_sysdir) and not os.path.islink(personas_sysdir):
        try:
            copyfile(personas_sysdir, personas_userdir)
            os.rename(personas_sysdir, personas_sysdir + ".orig")
            os.symlink(personas_userdir, personas_sysdir)
        except Exception as e:
            print(e)
            traceback.print_exc()

    # write config that preparation completed
    with open(userdir + "/lotc-prepare", "w") as f:
        f.write("finished")
        f.close()

    pass
