import sys
from array import *
from tkinter import *
import tkinter as Tk
from PIL import ImageTk, Image
from random import *
from GameButtons import GameButtons
import numpy as np
from Images import Images
from GameController import GameController

class GameView(Tk.Frame):
    scoreLabel = None
    field = None

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

        self.gameButtons = GameButtons()
        self.field = self.gameButtons.getFields()
        self.buttonIds = []

        self.gameController = GameController(self.scoreLabel, self.field)

        for i in range(0, self.field.shape[0]):
            for j in range(0, self.field.shape[1]):

                for image in Images:
                    if (self.gameButtons.getField(i,j) == image.getNumber()):
                        self.original = Image.open(image.getPath())
                        self.ph_im = ImageTk.PhotoImage(self.original)
                        self.b = Tk.Button(self.frame, image=self.ph_im, command=lambda i=i, j=j:self.gameController.buttonClicked(i, j, self.buttonIds))
                        self.b.image = self.ph_im
                        self.buttonIds.append(self.b)
                self.b.grid(row=i + 1,  column= j)

    def getScoreLabel(self):
        return self.scoreLabel
    
    def setScoreLabel(self, score):
        self.scoreLabel.config(text=score)

if __name__ == "__main__": 
    root=Tk.Tk()
    app = GameView(root)   
    root.mainloop()