from tkinter import *
from toolbar import toolbar
from menubar import menubar
class app():
    def __init__(self, master):
        self.master = master
        master.title("UV lab")
        mytoolbar = toolbar(master, controller=self)
        mymenubar = menubar(master, controller=self, root= root)
          
    def greet(self):
        print("Greetings!")
    def hello(self):
        print("Hello!")


 
#menubar.add_command(label="Quit!", command=top.quit)
x = 500
y = 400
root = Tk()
#root.attributes("-fullscreen", True)

root.geometry(f'{x}x{y}')
my_gui = app(root)
#my_gui.minsize("800x480")
root.mainloop()



  