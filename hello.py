import sys
from array import *
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image

view = Tk()
view.title("cundy crash")

numberOfFields = 9

field =[[0 for x in range(numberOfFields)] for y in range(numberOfFields)]

for r in field:
    for c in r:
        print(c, end = " ")
    print()

b = Button(view, text = "hhhhhh")
b.pack()

original = Image.open("img/java.png") # load an image from the hard drive
original.show()

view.mainloop()