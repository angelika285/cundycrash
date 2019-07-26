from SelectedButton import SelectedButton
from Images import Images
from PIL import ImageTk, Image
import random
from Points import Points
from FieldAnalyzer import FieldAnalyzer

class GameController:
    
    def __init__(self, scoreLabel, field):
        self.pointsInstanz = Points()
        self.scoreLabel = scoreLabel
        self.field = field
        self.oneButtonIsSelected = False
        self.firstSelectedButton = None
        self.secondSelectedButton = None
        self.buttonIds = None
        self.updateScoreLabel()

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
        fieldAnalyzer = FieldAnalyzer(self.field, self.pointsInstanz, self.buttonIds)
        fieldAnalyzer.checkRow()
        fieldAnalyzer.checkColumn()
        self.updateScoreLabel()
        #self.checkRow()
        #self.checkColumn()

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

    def updateScoreLabel(self):
        self.scoreLabel.configure(text=self.pointsInstanz.points)