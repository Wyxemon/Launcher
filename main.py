from tkinter import INSERT
from PIL import Image
from customtkinter import CTkButton, CTkEntry, CTkOptionMenu, StringVar, CTkProgressBar, CTk, CTkImage, CTkLabel, CTkSlider
import os

# Obtener el directorio del script
script_dir = os.path.dirname(os.path.abspath(__file__))

class Window:
    root = CTk()
    root.geometry("1280x720+300+100")
    root.config(background="gray10")
    root.title("Wyxemon Launcher")
    root.iconbitmap(os.path.join(script_dir, "Logo.ico"))  # Ruta absoluta a Logo.ico
    root.maxsize(width=1280, height=720)
    root._set_appearance_mode(mode_string="system")
    
class Interfaz(Window):
    class ImagenFondo:
        img = Image.open(os.path.join(script_dir, "UI.png"))  # Ruta absoluta a UI.png
        
        img_ctk = CTkImage(dark_image=img, light_image=img, size=(830,830))
        panel = CTkLabel(Window.root, image=img_ctk, text="")
        panel.place(x=450, y=-2)

    class JugarBoton:
        jugar_boton = CTkButton(Window.root, text="Jugar", width=430, height=40, fg_color="#6F9939", text_color="gray10", command=(lambda: Functions.abrir_minecraft()), hover_color="#434122")
        jugar_boton.place(x=10, y=670)
        
    class VersionMenu:
        version_label = CTkOptionMenu(Window.root, values=["1.20.1", "1.20.1 - Forge"], text_color="gray10", fg_color="lightgrey", button_color="darkorange1", button_hover_color="#434122")
        version_label.place(x=10, y=635)
    
    class NombreEntry:
        @staticmethod
        def leer_nombre():
            with open(os.path.join(script_dir, "login_name.txt"), encoding="UTF-8") as archivo:
                return archivo.read()
        
        nombre_entry = CTkEntry(Window.root, fg_color="gray10", text_color="lightgrey", bg_color="#242424", height=30, width=255, placeholder_text="Nombre de Usuario")
        nombre_entry.place(x=155, y=634)
        if leer_nombre() == "":
            pass
        else: 
            nombre_entry.insert(INSERT, leer_nombre())
        
    class ConfirmarNombreButton: 
        confirmar_nombre = CTkButton(Window.root, text="✓", width=10, height=30, text_color="gray10", fg_color="darkorange1", command=lambda: Functions.cambiar_nombre(), hover_color="#434122")
        confirmar_nombre.place(x=412, y=634)
        
    class MemoriaRamMenu:
        
        def read_ram():
            with open(os.path.join(script_dir, "ram_log.txt"), encoding="UTF-8") as archivo:
                return archivo.read()
        
        optionmenu_var = StringVar(value=read_ram() + " GB")
        
        memoria_ram = CTkOptionMenu(Window.root, values=["4 GB", "5 GB","6 GB", "7 GB", "8 GB", "9 GB", "10 GB", "11 GB", "12 GB", "13 GB", "14 GB", "15 GB", "16 GB"], text_color="gray10", fg_color="lightgrey", button_color="lightgrey", hover=True, variable=optionmenu_var)
        memoria_ram.place(x=268, y=600)
        
        confirmar_ram = CTkButton(Window.root, text="✓", width=10, height=30, text_color="gray10", fg_color="darkorange1", command=lambda: Functions.get_ram(), hover_color="#434122")
        confirmar_ram.place(x=412, y=599)
    
    class Settings:
        img = Image.open(os.path.join(script_dir, "Settings.png"))
        
        img_ctk = CTkImage(dark_image=img, light_image=img)
        panel = CTkButton(Window.root, image=img_ctk, text="", fg_color="lightgrey", width=20, bg_color="gray10", hover_color="#434122", border_color="gray10")
        panel.place(x=405, y=10)
    
    class Music:
        
        img = Image.open(os.path.join(script_dir, "Volume.png"))
        img_ctk = CTkImage(dark_image=img, light_image=img)
        panel = CTkButton(Window.root, image=img_ctk, text="", fg_color="lightgrey", width=20, bg_color="gray10", hover_color="#434122", border_color="gray10")
        panel.place(x=365, y=10)
        
        def slider_event(value):
            from pygame import mixer
            mixer.init()
            Interfaz.Music.mixer.music.set_volume(value)
            
        slider = CTkSlider(Window.root, from_=0, to=1, width=87, command=slider_event, button_color="darkorange1")
        slider.place(x=360, y=45)

        number = slider_event
        from pygame import mixer
        mixer.init()
        mixer.music.load("Gibran Alcocer - Solas (Cover).mp3")
        mixer.music.play(-1)
        mixer.music.set_volume(0.5)
        # Carga el archivo de música
        mixer.music.play()
                  
class Functions:
    class Intro:

        img = Image.open(os.path.join(script_dir, "WYXEMON STUDIOS.png"))
        
        img_ctk = CTkImage(light_image=img,dark_image=img, size=(1282,730))
        label_img = CTkLabel(Window.root, image=img_ctk, text="")
        label_img.place(x=-2, y=-2)

        progress_bar = CTkProgressBar(Window.root, mode="indeterminate", orientation="horizontal", progress_color="darkorange1", width=900, height=20, fg_color="black", bg_color="black")
        progress_bar.place(x=200, y=410)
        progress_bar.set(0)
        progress_bar.start()
        
    def destroy_intro():
        Functions.Intro.label_img.destroy()
        Functions.Intro.progress_bar.destroy()
    
    @staticmethod
    def get_ram():
        ram_GB = Interfaz.MemoriaRamMenu.memoria_ram.get()
        print(ram_GB)
        ram = ram_GB.replace(" GB", "")
        with open(os.path.join(script_dir, "ram_log.txt"), "w", encoding="UTF-8") as archivo:
            archivo.write(ram)
    
    def read_ram():
        with open(os.path.join(script_dir, "ram_log.txt"), encoding="UTF-8") as archivo:
            return archivo.read()
        
    @staticmethod
    def abrir_minecraft():
        import subprocess
        import os
        import minecraft_launcher_lib
        import ctypes

        ram = Functions.read_ram()

        def install_and_launch_minecraft(version_name, max_ram_gb=ram):
            # Definir el directorio de Minecraft
            minecraft_dir = os.path.expanduser('~/.minecraft')
            os.makedirs(minecraft_dir, exist_ok=True)
            # Instalar la versión especificada de Minecraft
            print(f"Instalando Minecraft {version_name}...")
            minecraft_launcher_lib.install.install_minecraft_version(version_name, minecraft_dir)

            # Configurar los argumentos del juego
            options = {
                "username": Interfaz.NombreEntry.leer_nombre(),  # Puedes cambiar el nombre de usuario aquí
                "uuid": "00000000-0000-0000-0000-000000000000",
                "token": "00000000000000000000000000000000"
            }

            # Obtener el comando para iniciar Minecraft
            minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(version_name, minecraft_dir, options)

            # Ajustar los argumentos JVM para usar la cantidad deseada de memoria RAM
            max_ram_arg = f"-Xmx{int(ram)}G"
            min_ram_arg = f"-Xms{int(ram)}G"

            # Insertar los argumentos de memoria en los argumentos del comando
            for i, arg in enumerate(minecraft_command):
                if arg.startswith("-Xmx") or arg.startswith("-Xms"):
                    minecraft_command.pop(i)

            minecraft_command = minecraft_command[:1] + [max_ram_arg, min_ram_arg] + minecraft_command[1:]

            # Variables de entorno para forzar el uso de la GPU
            env = os.environ.copy()
            env['CUDA_VISIBLE_DEVICES'] = '0'  # Asegurarse de usar la GPU 0 (ajustar según sea necesario)

            # Configuración para usar la GPU dedicada en Windows
            env['RadeonSettings'] = 'HighPerformance'
            env['__GL_THREADED_OPTIMIZATIONS'] = '1'
            env['__GL_SYNC_TO_VBLANK'] = '0'
            env['__GL_YIELD'] = 'NOTHING'

            # Establecer el ejecutable de Java para usar la GPU de alto rendimiento
            java_path = os.path.join(minecraft_dir, 'runtime', 'jre-x64', 'bin', 'javaw.exe')
            if os.path.exists(java_path):
                env['JAVA_HOME'] = java_path
                subprocess.run(['nvidia-smi', '-c', 'EXCLUSIVE_PROCESS', '-i', '0'])

            # Imprimir el comando que se va a ejecutar
            print("Comando para iniciar Minecraft:", " ".join(minecraft_command))
            # Ejecutar Minecraft ocultando la consola
            si = subprocess.STARTUPINFO()
            si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            si.wShowWindow = subprocess.SW_HIDE

            subprocess.Popen(minecraft_command, env=env, startupinfo=si)
            # Ocultar la consola principal (si se está ejecutando desde una consola)
            


        if __name__ == '__main__':
            # Especificar la versión oficial que quieres instalar y la cantidad de RAM (en GB)
            official_version = '1.20.1'
            ram_allocation_gb = int(ram)  # Cambia esto para ajustar la cantidad de RAM
            install_and_launch_minecraft(official_version, ram_allocation_gb)

        # Ocultar la consola principal (si se está ejecutando desde una consola)
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

    @staticmethod
    def cambiar_nombre():
        with open(os.path.join(script_dir, "login_name.txt"), "w", encoding="UTF-8") as archivo:
            archivo.write(Interfaz.NombreEntry.nombre_entry.get())
            print(Interfaz.NombreEntry.nombre_entry.get())

        
# Inicializar la ventana principal
Window.root.after(1534, lambda: Functions.destroy_intro())
Window.root.after(0, lambda: Functions.Intro())

app = Window()

Window.root.mainloop()
Interfaz.Music.mixer.music.stop()