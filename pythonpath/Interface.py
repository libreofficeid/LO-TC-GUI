import uno
from MainDialog import MainDialog

if __name__ == "__main__":
    """ Connect to LibreOffice proccess.
    1) Start the office in shell with command:
    soffice "--accept=socket,host=127.0.0.1,port=2002,tcpNoDelay=1;urp;StarOffice.ComponentContext" --norestore
    2) Run script
    """

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

    try:
        ctx = remote_ctx  # IDE
        print("disini remote")
    except:
        ctx = uno.getComponentContext()  # UI

    # get desktop
    desktop = ctx.getByName("/singletons/com.sun.star.frame.theDesktop")

    # get document
    document = desktop.getCurrentComponent()

    main_dialog = MainDialog(ctx=ctx)
    main_dialog.showDialog()