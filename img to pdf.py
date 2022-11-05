"""
FUENTE: https://es.acervolima.com/convierta-imagenes-a-pdf-usando-tkinter-python/
"""

import tkinter
from tkinter.filedialog import askopenfilenames
import img2pdf
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.geometry('400x200')
root.resizable(0, 0)
root.iconbitmap("c.ico")
def select_file():
    global file_names
    file_names = askopenfilenames(initialdir="/",
                                  title="Select File")

def image_to_pdf():
    for index, file_name in enumerate(file_names):
        with open(f"file {index}.pdf", "wb") as f:
            f.write(img2pdf.convert(file_name))


def images_to_pdf():
    with open(f"file.pdf", "wb") as f:
        f.write(img2pdf.convert(file_names))

frame = customtkinter.CTkFrame(master=root,
                               width=399,
                               height=200,
                               corner_radius=10,
                               fg_color=("white", "gray10"))
frame.pack(padx=80, pady=17)

text_var = tkinter.StringVar(value="IMAGE CONVERSION")
label = customtkinter.CTkLabel(master=frame,
                               textvariable=text_var,
                               width=150,
                               height=30,
                               corner_radius=8,
                               bg_color=("gray10"),
                               text_color=("white"))
label.place(relx=0.5, rely=0.1, anchor=tkinter.N)


boton1 = customtkinter.CTkButton(master=root,
                                 width=10,
                                 height=30,
                                 border_width=0,
                                 corner_radius=8,
                                 text="Select Images",
                                 command=select_file)
boton1.place(relx=0.5, rely=0.55, anchor=tkinter.S)


boton2 = customtkinter.CTkButton(master=root,
                                 width=10,
                                 height=32,
                                 border_width=0,
                                 corner_radius=8,
                                 text="Image to PDF",
                                 command=image_to_pdf)
boton2.place(relx=0.5, rely=0.6, anchor=tkinter.NE)


boton3 = button = customtkinter.CTkButton(master=root,
                                 width=10,
                                 height=32,
                                 border_width=0,
                                 corner_radius=8,
                                 text="Images to PDF",
                                 command=images_to_pdf)
button.place(relx=0.5, rely=0.6, anchor=tkinter.NW)


root.mainloop()