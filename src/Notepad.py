from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import *
from datetime import datetime
from tkinter.colorchooser import askcolor
import webbrowser

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
                choice = askyesnocancel("Custom-Notepad", "Do you want to save changes?")
                if choice:
                    writing()
                    root.destroy()
                elif choice is None:
                    pass
                else:
                    root.destroy()
            else:
                root.destroy()
        except:
            pass

    # Edit Menu :

    def Cut():
        try:
            text.clipboard_clear()
            text.clipboard_append(text.selection_get())
            text.delete(SEL_FIRST, SEL_LAST)
        except:
            pass
    
    def Copy():
        try:
            text.clipboard_clear()
            text.clipboard_append(text.selection_get())
        except:
            pass

    def Paste():
        try:
            data = text.selection_get(selection = "CLIPBOARD")
            text.insert(INSERT, data)
        except:
            pass

    def Delete():
        try:
            text.delete(SEL_FIRST, SEL_LAST)
        except:
            pass

    def Clear_screen():
        text.delete(1.0, END)

    # Insert Menu : 

    def Date():
        now = datetime.now()
        data = (str(now.strftime("%d/%m/%Y")) + "\n")
        text.insert(INSERT, data)
    
    def Time():
        now = datetime.now()
        data = (str(now.strftime("%H:%M:%S")) + "\n")
        text.insert(INSERT, data)

    def Date_and_time():
        now = datetime.now()
        data = (str(now.strftime("%d/%m/%Y %H:%M:%S")) + "\n")
        text.insert(INSERT, data)

    # Format Menu : 

    def Text_Colour():
        (triple,color) = askcolor()
        if(color):
            text.config(fg = color)
    
    def No_Format():
        try:
            text.tag_remove("bold", "sel.first", "sel.last")
            text.tag_remove("italic", "sel.first", "sel.last")
            text.tag_remove("underline", "sel.first", "sel.last")
            text.tag_remove("highlight", "sel.first", "sel.last")
            text.config(font = ("Agency FB", 20))
        except:
            pass

    def Bold():
        try:
            text.tag_add("bold", "sel.first", "sel.last")
            text.tag_config("bold",font = ("Agency FB", 20, "bold"))
        except:
            pass

    def Italic():
        try:
            text.tag_add("italic", "sel.first", "sel.last")
            text.tag_config("italic",font = ("Agency FB", 20, "italic"))
        except:
            pass

    def Underline():
        try:
            text.tag_add("underline", "sel.first", "sel.last")
            text.tag_config("underline",font = ("Agency FB", 20, "underline"))
        except:
            pass

    def Highlight():
        try:
            text.tag_add("highlight", "sel.first", "sel.last")
            text.tag_config("highlight", background = "yellow", foreground = "black")
        except:
            pass

    # Personalize Menu : 

    def Background():
        (triple,color) = askcolor()
        if(color):
            text.config(bg = color)

    # Help Menu : 

    def View_help():
        webbrowser.open("https://github.com/SVijayB/Custom-notepad")
    
    def Feedback():
        webbrowser.open("https://github.com/SVijayB/Custom-notepad/issues/new/choose")

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
    format_menu.add_command(label = "Bold", command = Bold)
    format_menu.add_command(label = "Italic", command = Italic)
    format_menu.add_command(label = "Underline", command = Underline)
    format_menu.add_command(label = "Highlight Text", command = Highlight)
    format_menu.add_command(label = "Remove Format", command = No_Format)

    personalize_menu = Menu(root, tearoff=False)
    main_menu.add_cascade(label = "Personalize", menu = personalize_menu)
    personalize_menu.add_command(label = "Background", command = Background)
    personalize_menu.add_command(label = "Text", command = Text_Colour)

    help_menu = Menu(root, tearoff=False)
    main_menu.add_cascade(label = "Help", menu = help_menu)
    help_menu.add_command(label = "View Help", command = View_help)
    help_menu.add_command(label = "Send Feedback", command = Feedback)

    text = Text(root, height = 17, width = 70, font = ("Agency FB", 20))
    scrollbar = Scrollbar(root, command = text.yview)
    scrollbar.config(command = text.yview)
    text.config(yscrollcommand = scrollbar.set)
    scrollbar.pack(side = RIGHT, fill=Y)
    text.pack()
    root.resizable(0,0)
    root.protocol("WM_DELETE_WINDOW",Close)

    root.mainloop()