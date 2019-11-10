IMPLE_NAME = "id.libreoffice.themechanger"

def create(ctx, *args):
    try:
        import ThemeChanger.Interface
        return ThemeChanger.Interface.run_dialog(IMPLE_NAME, ctx, *args)
    except Exception as e:
        print(e)

import unohelper
g_ImplementationHelper = unohelper.ImplementationHelper()
g_ImplementationHelper.addImplementation(
    create, IMPLE_NAME, (IMPLE_NAME,),)