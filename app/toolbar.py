from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import os

class toolbar(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        toolbar = Frame(self.master, bd=1, relief=RAISED)
        #sep = ttk.Separator(toolbar) 
        ## New file 
        self.new_img = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__), r"icons\new-document.png")))
        NewFile = Button(toolbar, image=self.new_img, relief=FLAT) ##New file add command
        #NewFile.image = self.new_img
        NewFile.pack(side=LEFT, padx=2, pady=2)

        ## open file
        self.open_img = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__), r"icons\open.png")))
        OpenFile = Button(toolbar, image=self.open_img, relief=FLAT) ##open file add command
        OpenFile.pack(side=LEFT, padx=2, pady=2)

        ## save file
        self.save_img = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__), r"icons\save_file.png")))
        SaveFile = Button(toolbar, image=self.save_img, relief=FLAT) ##save file add command
        SaveFile.pack(side=LEFT, padx=2, pady=2)
        
        ttk.Separator(toolbar,orient='vertical').place(relx=0.155, rely=0, relwidth=0.5, relheight=1)
        ## print file
        self.print_img = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__), r"icons\printer.png")))
        PrintFile = Button(toolbar, image=self.print_img, relief=FLAT) ##print file add command
        PrintFile.pack(side=LEFT, padx=2, pady=2)

        ttk.Separator(toolbar,orient='vertical').place(relx=0.208, rely=0, relwidth=0.5, relheight=1)

        ## cut file
        self.cut_img = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__), r"icons\cut.png")))
        CutFile = Button(toolbar, image=self.cut_img, relief=FLAT) ##cut file add command
        CutFile.pack(side=LEFT, padx=2, pady=2)

        ## copy file
        self.copy_img = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__), r"icons\copy.png")))
        CopyFile = Button(toolbar, image=self.copy_img, relief=FLAT) ##copy file add command
        CopyFile.pack(side=LEFT, padx=2, pady=2)

        ## paste file
        self.paste_img = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__), r"icons\paste.png")))
        PasteFile = Button(toolbar, image=self.paste_img, relief=FLAT) ##paste file add command
        PasteFile.pack(side=LEFT, padx=2, pady=2)

        ttk.Separator(toolbar,orient='vertical').place(relx=0.36, rely=0, relwidth=0.5, relheight=1)

        ## delete file
        self.delete_img = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__), r"icons\trash.png")))
        DeleteFile = Button(toolbar, image=self.delete_img, relief=FLAT) ##delete file add command
        DeleteFile.pack(side=LEFT, padx=2, pady=2)

        ## undo file
        self.undo_img = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__), r"icons\undo.png")))
        UndoFile = Button(toolbar, image=self.undo_img, relief=FLAT) ##undo file add command
        UndoFile.pack(side=LEFT, padx=2, pady=2)

        toolbar.pack(side=TOP, fill=X) 