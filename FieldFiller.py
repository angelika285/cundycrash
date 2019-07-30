import random
from SelectedButton import SelectedButton
from Images import Images
from PIL import ImageTk, Image

class FieldFiller:

    def __init__(self, field, buttonIds):
        self.field = field
        self.buttonIds = buttonIds

    def changeColumnFieldValues(self, sameValues, row, column):
        for row in reversed(range(0, row)):
            if row >= sameValues:
                self.field[row][column] = self.field[row-sameValues][column]
            else:
                self.field[row][column] = random.randint(0,5)
            button = SelectedButton(row, column, self.buttonIds)
            self.changePicture(button)

    def changeRowFieldValues(self, sameValues, row, column):
        for column in range(column, column+sameValues):
            actualRow = row
            for actualRow in reversed(range(0, actualRow+1)):
                if actualRow > 0:
                    self.field[actualRow][column] = self.field[actualRow-1][column]
                else:
                    self.field[actualRow][column] = random.randint(0,5)
                button = SelectedButton(actualRow, column, self.buttonIds)
                self.changePicture(button)

    def changePicture(self, button):
        for image in Images:
            if self.field[button.row][button.column] == image.getNumber():
                self.originalImage = Image.open(image.getPath())
                self.photoImage = ImageTk.PhotoImage(self.originalImage)
                button.button.configure(image=self.photoImage)
                button.button.image = self.photoImage