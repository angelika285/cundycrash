import sys
from array import *
from tkinter import *
import tkinter as Tk
from PIL import ImageTk, Image
from random import *
from gameButtons import gameButtons
import numpy as np

class game(Tk.Frame):
    def __init__(self,parent):
        Tk.Frame.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.parent.title("cundy crash")       
        self.parent.grid_rowconfigure(1,weight=1)
        self.parent.grid_columnconfigure(1,weight=1)

        self.frame = Tk.Frame(self.parent)  
        self.frame.pack(fill=Tk.X, padx=5, pady=5)

        #for r in self.a:
        #    for c in r:
        #       print(c, end = " ")
        #    print()

        self.gameButtons = gameButtons()
        for i in range(0, self.gameButtons.getFields().shape[0]):
            for j in range(0, self.gameButtons.getFields().shape[1]):
                self.b = Tk.Button(self.frame, text = self.gameButtons.getField(i, j))
                self.b.grid(row=i,  column= j)

if __name__ == "__main__": 
    root=Tk.Tk()
    app = game(root)   
    root.mainloop()


###########################################

#original = Image.open("img/java.png") # load an image from the hard drive