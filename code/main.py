def selector_interfaz():
    with open("Launcher/log/login_name.txt",encoding="UTF-8") as archivo:
        return archivo.read()
if selector_interfaz() == "":
    import login

import launcher