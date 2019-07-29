class ControllValues:

    def __init__(self, firstSelectedButton, secondSelectedButton):
        self.firstSelectedButton = firstSelectedButton
        self.secondSelectedButton = secondSelectedButton

    def firstSelectedButtonIsNotSecondSelectedButton(self):
        return not self.firstSelectedButton.button == self.secondSelectedButton.button

    def secondSelectedButtonIsNextToFirstSelectedButtonInTheSameRow(self):
        return self.secondButtonIsInSameRowAsFirstButton() and (self.secondButtonIsLeftOfFirstButton() or self.secondButtonIsRightOfFirstButton())

    def secondButtonIsInSameRowAsFirstButton(self):
        return self.firstSelectedButton.row == self.secondSelectedButton.row

    def secondButtonIsLeftOfFirstButton(self):
        return self.firstSelectedButton.column == self.secondSelectedButton.column -1

    def secondButtonIsRightOfFirstButton(self):
        return self.firstSelectedButton.column == self.secondSelectedButton.column +1

    def secondSelectedButtonIsNextToFirstSelectedButtonInTheSameColumn(self):
        return self.secondButtonIsInSameColumnAsFirstButton() and (self.secondButtonIsAboveOfFirstButton() or self.secondButtonIsUnderFirstButton())

    def secondButtonIsInSameColumnAsFirstButton(self):
        return self.firstSelectedButton.column == self.secondSelectedButton.column

    def secondButtonIsAboveOfFirstButton(self):
        return self.firstSelectedButton.row == self.secondSelectedButton.row -1

    def secondButtonIsUnderFirstButton(self):
        return self.firstSelectedButton.row == self.secondSelectedButton.row +1
