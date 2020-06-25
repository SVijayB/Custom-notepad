from tkinter import *
from Modules.functions import *
if __name__=="__main__":
    root = Tk()
    root.title("Custom-notepad")
    main_menu = Menu(root)
    commands = Menu(root)
    root.config(menu = main_menu)

    main_menu.add_cascade(label="File" , menu = commands)
    commands.add_command(label="New File", command = New_file)
    commands.add_command(label="Open...",command = Open_file)
    commands.add_command(label="Save As...",command = Save_as)
    commands.add_command(label="Exit",command = Close)