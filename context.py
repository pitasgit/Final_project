from browser import Browser

#punem Browser intr-un context al aplicatiei - asa are nevoie behave (face legatura intre clasa si behave)

def before_all(context):
    context.browser = Browser()

def after_all(context):
    context.browser.close()