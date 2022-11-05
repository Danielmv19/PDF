from tkPDFViewer import tkPDFViewer as pdf
from tkinter import*

root = Tk()
root.geometry('400x600')
v1 = pdf.ShowPdf()
v2 = v1.pdf_view(root, pdf_location="C:/Users/Administrador/Desktop/PYTHON/10.pdf")


root.mainloop()
