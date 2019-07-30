from SelectedButton import SelectedButton
from Images import Images
from PIL import ImageTk, Image
import random
from Points import Points
from FieldAnalyzer import FieldAnalyzer
from ControllValues import ControllValues

class GameController:
    
    def __init__(self, scoreLabel, fieldFiller):
        self.fieldFiller = fieldFiller
        self.pointsInstanz = Points()
        self.scoreLabel = scoreLabel
        self.field = fieldFiller.field
        self.oneButtonIsSelected = False
        self.firstSelectedButton = None
        self.secondSelectedButton = None
        self.buttonIds = fieldFiller.buttonIds
        self.updateScoreLabel()

    def buttonClicked(self, row, column):
        selectedButton = SelectedButton(row,column,self.buttonIds)
        if not self.oneButtonIsSelected:
            self.firstButtonAction(selectedButton)
        else:
            controll = ControllValues(self.firstSelectedButton, selectedButton)
            if controll.firstSelectedButtonIsNotSecondSelectedButton() and (controll.secondSelectedButtonIsNextToFirstSelectedButtonInTheSameRow() or controll.secondSelectedButtonIsNextToFirstSelectedButtonInTheSameColumn()):
                self.secondButtonAction(selectedButton)
            elif not controll.firstSelectedButtonIsNotSecondSelectedButton():
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
        fieldAnalyzer.checkField()
        if fieldAnalyzer.foundMoreThanOne == False:
            self.returnButtonsAction()
        self.updateScoreLabel()

    def returnButtonsAction(self):
        self.changePictures()

    def disselectFirstButtonAction(self):
        self.firstSelectedButton.button.configure(highlightbackground='#e8e8e8')
        self.oneButtonIsSelected = False

    def changePictures(self):
        self.changeFieldValues()
        self.fieldFiller.changePicture(self.firstSelectedButton)
        self.fieldFiller.changePicture(self.secondSelectedButton)

    def changeFieldValues(self):
        temp = self.field[self.firstSelectedButton.row][self.firstSelectedButton.column]
        self.field[self.firstSelectedButton.row][self.firstSelectedButton.column] = self.field[self.secondSelectedButton.row][self.secondSelectedButton.column]
        self.field[self.secondSelectedButton.row][self.secondSelectedButton.column] = temp

    def updateScoreLabel(self):
        self.scoreLabel.configure(text=self.pointsInstanz.points)