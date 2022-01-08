from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import os

class toolbar(Frame):
    def __init__(self, parent, controller, root):
        Frame.__init__(self, parent)
        self.root = root
        self.controller = controller
        toolbar = Frame(self.master, bd=1, relief=RAISED)
        #sep = ttk.Separator(toolbar) 
        ## New file 
        self.new_img = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__), r"icons\new-document.png")))
        NewFile = Button(toolbar, image=self.new_img, relief=FLAT) ##New file add command
        #NewFile.image = self.new_img
        NewFile.grid(column=0,row=0,padx=2, pady=2)

        ## open file
        self.open_img = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__), r"icons\open.png")))
        OpenFile = Button(toolbar, image=self.open_img, relief=FLAT) ##open file add command
        OpenFile.grid(column=1,row=0,padx=2, pady=2)

        ## save file
        self.save_img = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__), r"icons\save_file.png")))
        SaveFile = Button(toolbar, image=self.save_img, relief=FLAT) ##save file add command
        SaveFile.grid(column=2,row=0,padx=2, pady=2)
        
        ttk.Separator(toolbar,orient='vertical').place(x=78, y=0, height=self.root.winfo_screenwidth())

        ## print file
        self.print_img = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__), r"icons\printer.png")))
        PrintFile = Button(toolbar, image=self.print_img, relief=FLAT) ##print file add command
        PrintFile.grid(column=3,row=0,padx=2, pady=2)

        ttk.Separator(toolbar,orient='vertical').place(x=104, y=0, height=self.root.winfo_screenwidth())
        

        ## cut file
        self.cut_img = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__), r"icons\cut.png")))
        CutFile = Button(toolbar, image=self.cut_img, relief=FLAT) ##cut file add command
        CutFile.grid(column=4,row=0,padx=2, pady=2)

        ## copy file
        self.copy_img = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__), r"icons\copy.png")))
        CopyFile = Button(toolbar, image=self.copy_img, relief=FLAT) ##copy file add command
        CopyFile.grid(column=5,row=0,padx=2, pady=2)

        ## paste file
        self.paste_img = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__), r"icons\paste.png")))
        PasteFile = Button(toolbar, image=self.paste_img, relief=FLAT) ##paste file add command
        PasteFile.grid(column=6,row=0,padx=2, pady=2)

        ttk.Separator(toolbar,orient='vertical').place(x=181, y=0, height=self.root.winfo_screenwidth())

        ## delete file
        self.delete_img = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__), r"icons\trash.png")))
        DeleteFile = Button(toolbar, image=self.delete_img, relief=FLAT) ##delete file add command
        DeleteFile.grid(column=7,row=0,padx=2, pady=2)

        ## undo file
        self.undo_img = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__), r"icons\undo.png")))
        UndoFile = Button(toolbar, image=self.undo_img, relief=FLAT) ##undo file add command
        UndoFile.grid(column=8,row=0,padx=2, pady=2)

        ttk.Separator(toolbar,orient='vertical').place(x=234, y=0, height=self.root.winfo_screenwidth())

        toolbar.grid(column=0,row=0)
        root.config(menu=toolbar)  