from SelectedButton import SelectedButton
from Images import Images
from PIL import ImageTk, Image
import random
from Points import Points

class GameController:
    
    def __init__(self, scoreLabel, field):
        self.pointsInstanz = Points()
        self.scoreLabel = scoreLabel
        self.field = field
        self.oneButtonIsSelected = False
        self.firstSelectedButton = None
        self.secondSelectedButton = None
        self.buttonIds = None

    def buttonClicked(self, row, column, buttonIds):
        self.buttonIds = buttonIds
        selectedButton = SelectedButton(row,column,buttonIds)
        if not self.oneButtonIsSelected:
            self.firstButtonAction(selectedButton)
        elif self.firstSelectedButtonIsNotSecondSelectedButton(selectedButton) and (self.secondSelectedButtonIsNextToFirstSelectedButtonInTheSameRow(selectedButton) or self.secondSelectedButtonIsNextToFirstSelectedButtonInTheSameColumn(selectedButton)):
            self.secondButtonAction(selectedButton)
        elif not self.firstSelectedButtonIsNotSecondSelectedButton(selectedButton):
            self.disselectFirstButtonAction()
        else:
            self.disselectFirstButtonAction()
            self.firstButtonAction(selectedButton)

    def firstButtonAction(self, selectedButton):
        self.firstSelectedButton = selectedButton
        self.firstSelectedButton.button.configure(highlightbackground='#3E4149')
        #self.firstSelectedButton.button.flash()
        self.oneButtonIsSelected = True
    
    def secondButtonAction(self, selectedButton):
        self.secondSelectedButton = selectedButton
        self.disselectFirstButtonAction()
        self.changePictures()
        self.checkRow()
        self.checkColumn()

    def disselectFirstButtonAction(self):
        self.firstSelectedButton.button.configure(highlightbackground='#e8e8e8')
        self.oneButtonIsSelected = False

    def changePictures(self):
        self.changeFieldValues()
        self.changePicture(self.firstSelectedButton)
        self.changePicture(self.secondSelectedButton)
    
    def changePicture(self, button):
        for image in Images:
            if self.field[button.row][button.column] == image.getNumber():
                self.originalImage = Image.open(image.getPath())
                self.photoImage = ImageTk.PhotoImage(self.originalImage)
                button.button.configure(image=self.photoImage)
                button.button.image = self.photoImage

    def changeFieldValues(self):
        temp = self.field[self.firstSelectedButton.row][self.firstSelectedButton.column]
        self.field[self.firstSelectedButton.row][self.firstSelectedButton.column] = self.field[self.secondSelectedButton.row][self.secondSelectedButton.column]
        self.field[self.secondSelectedButton.row][self.secondSelectedButton.column] = temp

    def firstSelectedButtonIsNotSecondSelectedButton(self, selectedButton):
        return not self.firstSelectedButton.button == selectedButton.button

    def secondSelectedButtonIsNextToFirstSelectedButtonInTheSameRow(self, selectedButton):
        return self.secondButtonIsInSameRowAsFirstButton(selectedButton) and (self.secondButtonIsLeftOfFirstButton(selectedButton) or self.secondButtonIsRightOfFirstButton(selectedButton))

    def secondButtonIsInSameRowAsFirstButton(self, selectedButton):
        return self.firstSelectedButton.row == selectedButton.row

    def secondButtonIsLeftOfFirstButton(self, selectedButton):
        return self.firstSelectedButton.column == selectedButton.column -1

    def secondButtonIsRightOfFirstButton(self, selectedButton):
        return self.firstSelectedButton.column == selectedButton.column +1

    def secondSelectedButtonIsNextToFirstSelectedButtonInTheSameColumn(self, selectedButton):
        return self.secondButtonIsInSameColumnAsFirstButton(selectedButton) and (self.secondButtonIsAboveOfFirstButton(selectedButton) or self.secondButtonIsUnderFirstButton(selectedButton))

    def secondButtonIsInSameColumnAsFirstButton(self, selectedButton):
        return self.firstSelectedButton.column == selectedButton.column

    def secondButtonIsAboveOfFirstButton(self, selectedButton):
        return self.firstSelectedButton.row == selectedButton.row -1

    def secondButtonIsUnderFirstButton(self, selectedButton):
        return self.firstSelectedButton.row == selectedButton.row +1

    def checkRow(self):
        for row in range(0, self.field.shape[0]):
            for column in range(0, self.field.shape[1]-2):
                self.pointsInstanz.setEarnedPoints(self.checkItemInRow(row, column))
        self.setScoreLabel(self.pointsInstanz.points)

    def checkItemInRow(self, row, column):
        sameValue = 1
        # TODO: bei gefundenem paar reihe von neu beginnen
        while column < 8 and self.field[row][column] == self.field[row][column+1]:
            sameValue += 1
            column += 1
        if sameValue > 2:
            self.changeRowFieldValues(sameValue ,row, column-sameValue+1)
        return sameValue

    def checkColumn(self):
        for row in reversed(range(0+2, self.field.shape[0])):
            for column in range(0, self.field.shape[1]):
                #self.points += self.checkForEarnedPoints(self.checkItemInColumn(row, column))
                self.pointsInstanz.setEarnedPoints(self.checkItemInColumn(row, column))
                column += 1
        self.setScoreLabel(self.pointsInstanz.points)

    def checkItemInColumn(self, row, column):
        # TODO: bei gefundenem paar zeile von neu beginnen
        sameValue = 1
        while row > 0 and self.field[row][column] == self.field[row-1][column]:
            sameValue += 1
            row -= 1
        if sameValue > 2:
            self.changeColumnFieldValues(sameValue, row+sameValue, column)
        return sameValue

    def changeColumnFieldValues(self, sameValues, row, column):
        for row in reversed(range(0, row)):
            if row >= sameValues:
                self.field[row][column] = self.field[row-sameValues][column]
            else:
                self.field[row][column] = random.randint(0, 6)
            button = SelectedButton(row, column, self.buttonIds)
            self.changePicture(button)

    def changeRowFieldValues(self, sameValues, row, column):
        for column in range(column, column+sameValues):
            actualRow = row
            for actualRow in reversed(range(0, actualRow+1)):
                if actualRow > 0:
                    self.field[actualRow][column] = self.field[actualRow-1][column]
                else:
                    self.field[actualRow][column] = random.randint(0,6)
                button = SelectedButton(actualRow, column, self.buttonIds)
                self.changePicture(button)

    def setScoreLabel(self, score):
        self.scoreLabel.configure(text=score)