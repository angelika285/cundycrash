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
from FieldFiller import FieldFiller

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

        fieldFiller = FieldFiller(self.field, self.buttonIds)
        self.gameController = GameController(self.scoreLabel, fieldFiller)

        for i in range(0, self.field.shape[0]):
            for j in range(0, self.field.shape[1]):

                for image in Images:
                    if (self.gameButtons.getField(i,j) == image.getNumber()):
                        self.originalImage = Image.open(image.getPath())
                        self.photoImage = ImageTk.PhotoImage(self.originalImage)
                        self.button = Tk.Button(self.frame, image=self.photoImage, command=lambda i=i, j=j:self.gameController.buttonClicked(i, j), borderwidth=0, highlightthickness=0)
                        self.button.image = self.photoImage
                        self.buttonIds.append(self.button)
                self.button.grid(row=i + 1,  column= j)
        
        fieldFiller.field = self.field
        fieldFiller.buttonIds = self.buttonIds

if __name__ == "__main__": 
    root=Tk.Tk()
    app = GameView(root)   
    root.mainloop()