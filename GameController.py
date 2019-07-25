from SelectedButton import SelectedButton
from Images import Images
from PIL import ImageTk, Image

class GameController:
    
    def __init__(self, scoreLabel, field):
        self.points = 0
        self.scoreLabel = scoreLabel
        self.field = field
        self.oneButtonIsSelected = False
        self.firstSelectedButton = None
        self.secondSelectedButton = None

    def buttonClicked(self, row, column, buttonIds):
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
        self.oneButtonIsSelected = True
    
    def secondButtonAction(self, selectedButton):
        self.secondSelectedButton = selectedButton
        self.secondSelectedButton.button.configure(highlightbackground='#9c498c')
        self.changePictures()
        self.oneButtonIsSelected = False
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
            for column in range(0, self.field.shape[1]-3):
                self.points += self.checkForEarnedPoints(self.checkItemInRow(row, column))
        self.setScoreLabel(self.points)

    def checkItemInRow(self, row, column):
        sameValue = 1
        # TODO: bei gefundenem paar reihe von neu beginnen
        while column < 9 and self.field[row][column] == self.field[row][column+1]:
            sameValue += 1
            column += 1
        return sameValue

    def checkColumn(self):
        for row in range(0, self.field.shape[0]-3):
            for column in range(0, self.field.shape[1]):
                self.points += self.checkForEarnedPoints(self.checkItemInColumn(row, column))
                column += 1
        self.setScoreLabel(self.points)

    def checkItemInColumn(self, row, column):
        # TODO: bei gefundenem paar zeile von neu beginnen
        sameValue = 1
        while row < 10 and self.field[row][column] == self.field[row+1][column]:
            sameValue += 1
            row += 1
        return sameValue

    def checkForEarnedPoints(self, sameValues):
        if sameValues == 3:
            return 10
        elif sameValues == 4:
            return 20
        elif sameValues == 5:
            return 30
        elif sameValues == 6:
            return 40
        elif sameValues == 7:
            return 50
        elif sameValues == 8:
            return 60
        elif sameValues == 9:
            return 70
        elif sameValues == 10:
            return 80
        else:
            return 0

    def setScoreLabel(self, score):
        self.scoreLabel.configure(text=score)