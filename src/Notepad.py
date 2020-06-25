from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import askyesno
from Modules.edit_menu import *
from Modules.format_menu import *
from Modules.help_menu import *
from Modules.insert_menu import *
from Modules.personalize_menu import *

if __name__=="__main__":

    def writing():
        filename = filedialog.asksaveasfilename()
        if filename:
            content = text.get(1.0, END)
            open(filename, 'w').write(content)

    # Commands : 

    def New_file():
        try:
            if not text.compare("end-1c", "==", "1.0"):
                if askyesno("Custom-Notepad", "Do you want to save changes?"):
                    writing()
                else:
                    text.delete(1.0, END)
        except:
            pass

    def Open_file():
        try:
            if not text.compare("end-1c", "==", "1.0"):
                if askyesno("Custom-Notepad", "Do you want to save changes?"):
                    writing()
                    text.delete(1.0, END)
            file = open(filedialog.askopenfilename(), "r")
            text.delete(1.0, END)
            if(file!=""):
                content = file.read()
                text.insert(INSERT, content)
        except:
            pass

    def Save_as():
        try:
            if not text.compare("end-1c", "==", "1.0"):
                writing()
            else:
                if askyesno("Custom-Notepad", "Do you want to save an empty file?"):
                    writing()
        except:
            pass
    
    def Close():
        try:
            if not text.compare("end-1c", "==", "1.0"):
                if askyesno("Custom-Notepad", "Do you want to exit without saving?"):
                    root.destroy()
                else:
                    writing()
                    root.destroy()
            else:
                root.destroy()
        except:
            pass


    root = Tk()
    root.title("Custom-notepad")
    main_menu = Menu(root)
    root.config(menu = main_menu)

    commands = Menu(root, tearoff=False)
    main_menu.add_cascade(label = "File" , menu = commands)
    commands.add_command(label = "New File", command = New_file)
    commands.add_command(label = "Open...", command = Open_file)
    commands.add_command(label = "Save As...", command = Save_as)
    commands.add_command(label = "Exit", command = Close)

    edit_menu = Menu(root, tearoff=False)
    main_menu.add_cascade(label = "Edit" , menu = edit_menu)
    edit_menu.add_command(label = "Cut", command = Cut)
    edit_menu.add_command(label = "Copy", command = Copy)
    edit_menu.add_command(label = "Paste", command = Paste)
    edit_menu.add_separator()
    edit_menu.add_command(label = "Delete", command = Delete)
    edit_menu.add_command(label = "Clear Screen", command = Clear_screen)

    insert_menu = Menu(root, tearoff=False)
    main_menu.add_cascade(label = "Insert", menu = insert_menu)
    insert_menu.add_command(label = "Current Date", command = Date)
    insert_menu.add_command(label = "Current Time", command = Time)
    insert_menu.add_command(label = "Date And Time", command = Date_and_time)

    format_menu = Menu(root, tearoff=False)
    main_menu.add_cascade(label = "Format", menu = format_menu)
    format_menu.add_command(label = "Font", command = Text_Colour)
    format_menu.add_separator()
    format_menu.add_command(label = "No Format", command = No_Format)
    format_menu.add_command(label = "Bold", command = Bold)
    format_menu.add_command(label = "Italic", command = Italic)
    format_menu.add_command(label = "Underline", command = Underline)

    personalize_menu = Menu(root, tearoff=False)
    main_menu.add_cascade(label = "Personalize", menu = personalize_menu)
    personalize_menu.add_command(label = "Background", command = Background)
    personalize_menu.add_command(label = "Text", command = Text_Colour)

    help_menu = Menu(root, tearoff=False)
    main_menu.add_cascade(label = "Help", menu = help_menu)
    help_menu.add_command(label = "View Help", command = View_help)
    help_menu.add_command(label = "Send Feedback", command = Feedback)

    text = Text(root, height = 20, width = 85, font = ("Agency FB", 14))
    scrollbar = Scrollbar(root, command = text.yview)
    scrollbar.config(command = text.yview)
    text.config(yscrollcommand = scrollbar.set)
    scrollbar.pack(side = RIGHT, fill=Y)
    text.pack()
    root.resizable(0,0)
    root.mainloop()