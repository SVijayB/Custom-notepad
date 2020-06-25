from tkinter import *
from Modules.commands import *
from Modules.edit_menu import *
from format_menu import *
from Modules.help_menu import *
from Modules.insert_menu import *
from Modules.personalize_menu import *

if __name__=="__main__":
    root = Tk()
    root.title("Custom-notepad")
    main_menu = Menu(root)
    commands = Menu(root)
    root.config(menu = main_menu)

    main_menu.add_cascade(label = "File" , menu = commands)
    commands.add_command(label = "New File", command = New_file)
    commands.add_command(label = "Open...", command = Open_file)
    commands.add_command(label = "Save As...", command = Save_as)
    commands.add_command(label = "Exit", command = Close)

    edit_menu = Menu(root)
    main_menu.add_cascade(label = "Edit" , menu = edit_menu)
    edit_menu.add_command(label = "Cut", command = Cut)
    edit_menu.add_command(label = "Copy", command = Copy)
    edit_menu.add_command(label = "Paste", command = Paste)
    edit_menu.add_command(label = "Delete", command = Erase)
    edit_menu.add_command(label = "Clear Screen", command = Clear_screen)

    insert_menu = Menu(root)
    main_menu.add_cascade(label = "Insert", menu = insert_menu)
    insert_menu.add_command(label = "Current Date", command = Date)
    insert_menu.add_command(label = "Current Time", command = Time)
    insert_menu.add_command(label = "Date And Time", command = Date_and_time)

    format_menu = Menu(root)
    main_menu.add_cascade(label = "Format", menu = format_menu)
    format_menu.add_command(label = "Font", command = Text_Colour)
    format_menu.add_command(label = "No Format", command = No_Format)
    format_menu.add_command(label = "Bold", command = Bold)
    format_menu.add_command(label = "Italic", command = Italic)
    format_menu.add_command(label = "Underline", command = Underline)

    personalize_menu = Menu(root)
    main_menu.add_cascade(label = "Personalize", menu = personalize_menu)
    personalize_menu.add_command(label = "Background", command = Background)
    personalize_menu.add_command(label = "Text", command = Text_Colour)

    help_menu = Menu(root)
    main_menu.add_cascade(label = "Help", menu = help_menu)
    help_menu.add_command(label = "View Help", command = View_help)
    help_menu.add_command(label = "Send Feedback", command = Feedback)