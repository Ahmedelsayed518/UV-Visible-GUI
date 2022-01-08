from tkinter import *
from tkinter import ttk

class menubar(Frame):
    def __init__(self, parent, controller, root):
        Frame.__init__(self, parent)
        self.controller = controller
        self.root = root
        menubar = Menu(self.root)  
        
        file = Menu(menubar, tearoff=0)
        edit = Menu(menubar, tearoff=0) 

        #file menu###########
        file.add_command(label="New")  
        file.add_command(label="Open")  
        file.add_command(label="Save")  
        file.add_command(label="Save as...")  
        file.add_command(label="Close") 
        file.add_separator()   
        file.add_command(label="Exit")  
        menubar.add_cascade(label="File", menu=file)
        #######################

        #Edit menu#############
        edit.add_command(label="Undo")  
        edit.add_separator()  
        edit.add_command(label="Cut")  
        edit.add_command(label="Copy")  
        edit.add_command(label="Paste")  
        edit.add_command(label="Delete")  
        edit.add_command(label="Select All")  
        menubar.add_cascade(label="Edit", menu=edit)

        root.config(menu=menubar) 