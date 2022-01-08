from tkinter import *
from toolbar import toolbar
from menubar import menubar
from graph import graph
class app():
    def __init__(self, master):
        self.master = master
        master.title("UV lab")
        mytoolbar = toolbar(master, controller=self, root= root)
        mymenubar = menubar(master, controller=self, root= root)
        mygraph = graph(master, contoller=self, root = root,master= master)

 

x = 500
y = 400
root = Tk()
root.geometry(f'{x}x{y}')
my_gui = app(root)
root.mainloop()



  