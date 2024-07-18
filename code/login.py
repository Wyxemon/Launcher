import tkinter as tk
from PIL import ImageTk, Image
from customtkinter import CTkEntry, CTkButton

class Ventana:
    root = tk.Tk()
    root.resizable(width=False, height=False)
    root.geometry("700x500+500+200")
    root.title("Wyxemon Launcher")
    root.config(bg="gray10")
    root.iconbitmap("Launcher/image/Logo.ico")
    # Desactiva el botón de cierre
    root.protocol("WM_DELETE_WINDOW", lambda: None)

class ImagenFondo(Ventana):
    img = ImageTk.PhotoImage(Image.open("Launcher/image/Login.png"))
    panel = tk.Label(Ventana.root, image=img, bg="gray10")
    panel.place(x=-2, y=-2)

class InterfazInicio(Ventana):
    def __init__(self):
        super().__init__()
        
        self.text_inicio = tk.Label(text="Inicio de Sesión", bg="gray10", font=("Arial Black", 20), fg="white")
        self.text_inicio.place(x=435, y=10)
        
        self.entrada_inicio = CTkEntry(Ventana.root, text_color="white", bg_color="gray10", width=240, height=35, fg_color="#604B4B")
        self.entrada_inicio.place(x=437, y=60)
        
        self.entrada_inicio.insert(tk.INSERT, "Ingrese su nombre")
        self.boton_inicio = CTkButton(Ventana.root, text_color="white", bg_color="gray10", fg_color="#90BE53", width=240, text="Entrar", height=35)
        
        self.boton_inicio.place(x=437, y=110)
        self.boton_inicio.configure(command=self.iniciar_sesion)  # Corregido a 'configure'
        
    def iniciar_sesion(self):
        nombre_usuario = self.entrada_inicio.get()  # Obtener el texto ingresado
        if nombre_usuario == "Ingrese su nombre":
            error_label = tk.Label(Ventana.root, text="# Error de usuario", bg="gray10", fg="red")
            error_label.place(x=437, y=150)
            
        elif nombre_usuario == "":
            error_label = tk.Label(Ventana.root, text="# Error de usuario", bg="gray10", fg="red")
            error_label.place(x=437, y=150)
        
        else:
            with open("Launcher/log/login_name.txt", "w", encoding="UTF-8") as archivo:
                archivo.write(nombre_usuario)
                Ventana.root.destroy()
        
class Version:
    def __init__(self, version, posicion):
        self.version = version
        self.posicion = posicion
        
        version = tk.Label(Ventana.root, text=self.version, bg="gray10", fg="white")
        version.place(x=self.posicion, y=470)

interfaz = InterfazInicio()

version = Version("v0.1", 666)

Ventana.root.mainloop()