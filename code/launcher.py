import tkinter as tk
from PIL import ImageTk, Image
from customtkinter import CTkButton, CTkLabel, CTkEntry

class Window:
        root = tk.Tk()
        root.geometry("1280x720+300+100")
        root.config(background="gray10")
        root.title("Wyxemon Launcher")
        
        root.iconbitmap("Launcher/image/Logo.ico")

class Interfaz(Window):
        class ImagenFondo:
                img = ImageTk.PhotoImage(Image.open("Launcher/image/UI.png"))
                panel = tk.Label(Window.root, image=img, bg="gray10")
                panel.place(x=450, y=-2)

        class Jugar_Boton:
                jugar_boton = CTkButton(Window.root, text="Jugar", width=430, height=40, fg_color="#6F9939", text_color="gray10")
                jugar_boton.place(x=10, y=670)
                
        class Version_Label:
                version_label = CTkButton(Window.root, text=" 1.18.2 ", text_color="gray10", fg_color="#D6A71B", hover_color="#D6A71B")
                version_label.place(x=10, y=635)
        
        class Nombre_Entry:
                def leer_nombre():
                        with open("Launcher/log/login_name.txt", encoding = "UTF-8") as archivo:
                                return archivo.read() 
                        
                nombre_entry = CTkEntry(Window.root, fg_color="#E2E2E2", text_color="gray10", bg_color="gray10", height=30, width=287)
                nombre_entry.place(x=155, y=634)
                nombre_entry.insert(tk.INSERT, leer_nombre())
        
        class Servido:
                servidor_label = CTkButton(Window.root, text="", text_color="gray10", fg_color="#E2E2E2", hover_color="#E2E2E2")
                servidor_label.place(x=10, y=10)
                

app = Window()

Window.root.mainloop()