import sys
from array import *
from tkinter import *
import tkinter as Tk
from PIL import ImageTk, Image
from random import *
from gameButtons import gameButtons
import numpy as np
from images import Images

class gameView(Tk.Frame):
    scoreLabel = None

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

        scoreTextLabel = Label(self.frame, text="Score:")
        scoreTextLabel.grid(row=0, column=0)

        self.scoreLabel = Label(self.frame)
        self.scoreLabel.grid(row=0, column=1)

        self.gameButtons = gameButtons()
        for i in range(0, self.gameButtons.getFields().shape[0]):
            for j in range(0, self.gameButtons.getFields().shape[1]):

                for image in Images:
                    if (self.gameButtons.getField(i,j) == image.getNumber()):
                        self.original = Image.open(image.getPath())
                        self.ph_im = ImageTk.PhotoImage(self.original)
                        self.b = Tk.Button(self.frame, image=self.ph_im)
                        #self.b.config(bg=text_org_bg)
                        self.b.image = self.ph_im
                self.b.grid(row=i + 1,  column= j)

    def getScoreLabel(self):
        return self.scoreLabel
    
    def setScoreLabel(self, score):
        self.scoreLabel.config(text=score)

if __name__ == "__main__": 
    root=Tk.Tk()
    app = gameView(root)   
    root.mainloop()