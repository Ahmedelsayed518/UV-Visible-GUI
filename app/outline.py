from tkinter import *
from PIL import Image, ImageTk
class app:
    def __init__(self, master):
        self.master = master
        self.menubar = Menu(root)  
        master.title("UV lab")
        self.file = Menu(self.menubar, tearoff=0)
        self.edit = Menu(self.menubar, tearoff=0)   
        #self.label = Label(master, text="This is our first GUI!")
        #self.label.pack()

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

        #file menu###########
        self.file.add_command(label="New")  
        self.file.add_command(label="Open")  
        self.file.add_command(label="Save")  
        self.file.add_command(label="Save as...")  
        self.file.add_command(label="Close") 
        self.file.add_separator()   
        self.file.add_command(label="Exit")  
        self.menubar.add_cascade(label="File", menu=self.file)
        #######################

        #Edit menu#############
        self.edit.add_command(label="Undo")  
        self.edit.add_separator()  
        self.edit.add_command(label="Cut")  
        self.edit.add_command(label="Copy")  
        self.edit.add_command(label="Paste")  
        self.edit.add_command(label="Delete")  
        self.edit.add_command(label="Select All")  
        self.menubar.add_cascade(label="Edit", menu=self.edit)
        ###########################

        ## toolbar ###############3
        toolbar = Frame(self.master, bd=1, relief=RAISED)

        self.img = Image.open(r"D:\UV-Visible-GUI\app\Photo.png")
        eimg = ImageTk.PhotoImage(self.img)

        exitButton = Button(toolbar, image=eimg, relief=FLAT,
            command=master.quit)
        exitButton.image = eimg
        exitButton.pack(side=LEFT, padx=2, pady=2)

        toolbar.pack(side=TOP, fill=X)
        #self.master.config(menu=self.menubar)
        #self.toolbar.pack()
        root.config(menu=self.menubar) 
    def greet(self):
        print("Greetings!")
    def hello(self):
        print("Hello!")


 
#menubar.add_command(label="Quit!", command=top.quit)

root = Tk()
root.geometry("250x150+300+300")
my_gui = app(root)
 
root.mainloop()



  