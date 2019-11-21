#!/usr/bin/env python3

import uno
import unohelper
import os
import sys
import traceback
import subprocess
import shutil

#Popen(["soffice", "--accept=socket,host=127.0.0.1,port=2002,tcpNoDelay=1;urp;StarOffice.ComponentContext","--norestore"])

local_ctx = uno.getComponentContext()
resolver = local_ctx.ServiceManager.createInstance("com.sun.star.bridge.UnoUrlResolver")

try:
    remote_ctx = resolver.resolve("uno:socket,"
                                        "host=127.0.0.1,"
                                        "port=2002,"
                                        "tcpNoDelay=1;"
                                        "urp;"
                                        "StarOffice.ComponentContext")
except Exception as err:
    print(err)
    traceback.print_exc()
    exit(-1)


try:
    ctx = remote_ctx
except:
    ctx = uno.getComponentContext()

ps = ctx.getServiceManager().createInstanceWithContext('com.sun.star.util.PathSubstitution', ctx)

install_sysdir = uno.fileUrlToSystemPath(ps.getSubstituteVariableValue("$(instpath)"))
program_sysdir = install_sysdir + "/program"
personas_sysdir = install_sysdir + "/share/gallery"
userdir = uno.fileUrlToSystemPath(ps.getSubstituteVariableValue("$(userurl)"))
lotc_userdir = userdir + "/lotc-themes"
gallery_userdir = userdir + "/gallery"

RUNME = "import os;" \
        "import shutil;" \
        "os.remove('{0}');" \
        "os.rename('{1}','{0}');"

if os.path.exists(program_sysdir + "/intro.png.orig"):
    subprocess.call(["sudo","python","-c",RUNME.format(program_sysdir + "/intro.png", program_sysdir + "/intro.png.orig")])
    print("Rollback to system intro.png")
#    os.remove(program_sysdir + "/intro.png")
#    os.rename(program_sysdir + "/intro.png.orig", program_sysdir + "/intro.png")

if os.path.exists(program_sysdir + "/sofficerc.orig"):
    subprocess.call(["sudo","python","-c",RUNME.format(program_sysdir + "/sofficerc", program_sysdir + "/sofficerc.orig")])
    print("Rollback to system sofficerc")
#    os.remove(program_sysdir + "/sofficerc")
#    os.rename(program_sysdir + "/sofficerc.orig", program_sysdir + "/sofficerc")

if os.path.exists(personas_sysdir + "/personas.orig"):
    subprocess.call(["sudo","python","-c",RUNME.format(personas_sysdir + "/personas", personas_sysdir + "/personas.orig")])
    print("Rollback to system personas dir")
#    os.remove(personas_sysdir + "/personas")
#    os.rename(personas_sysdir + "/personas.orig", program_sysdir + "/personas")

if os.path.exists(lotc_userdir):
    shutil.rmtree(lotc_userdir)
    print("removed lotc-theme in userdir")

if os.path.exists(gallery_userdir + "/personas"):
    shutil.rmtree(gallery_userdir + "/personas")
    print("removed personas in userdir")

if os.path.exists(userdir + "/lotc-prepare"):
    os.remove(userdir + "/lotc-prepare")

print("Success!")
