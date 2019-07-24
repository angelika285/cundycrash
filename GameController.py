from SelectedButton import SelectedButton

class GameController:
    
    def __init__(self, scoreLabel, field):
        self.points = 0
        self.scoreLabel = scoreLabel
        self.field = field
        self.oneButtonIsSelected = False
        self.firstSelectedButton = None
        self.secondSelectedButton = None

    def buttonClicked(self, i, j, buttonIds):
        selectedButton = SelectedButton(i,j,buttonIds)
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
        self.oneButtonIsSelected = False

    def disselectFirstButtonAction(self):
        self.firstSelectedButton.button.configure(highlightbackground='#e8e8e8')
        self.oneButtonIsSelected = False

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

    def checkColumn(self):
        for row in range(0, self.field.shape[0]):
            for column in range(0, self.field.shape[1]-3):
                points += self.checkForEarnedPoints(self.checkItemInColumn(row, column))
        self.setScoreLabel(points)

    def checkItemInColumn(self, row, column):
        sameValue = 0
        while self.field[row, column] == self.field[row, column+1]:
            sameValue += 1
            column += 1
        return sameValue

    def checkForEarnedPoints(self, sameValues):
        switcher = {
            3: 10,
            4: 20,
            5: 30,
            6: 40,
            7: 50,
            8: 60,
            9: 70,
            10: 80
        }
        return 0

    def setScoreLabel(self, score):
        self.scoreLabel.config(text=score)