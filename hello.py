import sys
from array import *
from tkinter import *
import tkinter as tk
#from PIL import ImageTk, Image

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

img = tk.PhotoImage(file = "C:\python\img\java.gif")

panel = tk.Label(view, image = img)
panel.pack()

view.mainloop()