from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import askyesno
from Notepad import *

def New_file():
    if askyesno("Custom-Notepad", "Do you want to save changes?"):
        filename = filedialog.asksaveasfilename()
        if filename:
            data = content.get(1.0, END)
            open(filename, 'w').write(data)
    else:
        content.delete(1.0, END)

def Open_file():
    if askyesno("Custom-Notepad", "Do you want to save changes?"):
        filename = filedialog.asksaveasfilename()
        if filename:
            data = content.get(1.0, END)
            open(filename, 'w').write(data)

def Save_as():
    pass

def Close():
    pass