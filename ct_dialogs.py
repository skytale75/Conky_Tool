from tkinter import *

class Color_Box():

    def __init__(self, title):
        self.root = Tk()
        self.root.title(title)
        self.root.grid()

    def color_window(self):
        cb.frame = Frame(self.root)
        cb.frame.grid(row = 0, columnspan=3)
        cb.frame.grid_configure(sticky="NSEW")
        cb.frame.config(bg="black")

    def run(self):
        self.root.mainloop()


cb = Color_Box("Color Manager")
cb.run()