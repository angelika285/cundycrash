class GameController:
    
    def __init__(self, scoreLabel, field):
        self.points = 0
        self.scoreLabel = scoreLabel
        self.field = field
        self.oneButtonIsSelected = False
        self.firstSelectedButton = None
        self.rowOfFirstSelectedButton = None
        self.columnOfFirstSelectedButton = None
        self.secondSelectedButton = None

    def buttonClicked(self, i, j, buttenIds):
        if not self.oneButtonIsSelected:
            self.firstSelectedButton = self.getSelectedButton(i,j)
            self.rowOfFirstSelectedButton = i
            self.columnOfFirstSelectedButton = j
            buttenIds[self.firstSelectedButton].configure(highlightbackground='#3E4149')
            self.oneButtonIsSelected = True
        elif self.firstSelectedButtonIsNotSecondSelectedButton(i,j):
            self.secondSelectedButton = self.getSelectedButton(i,j)
            buttenIds[self.secondSelectedButton].configure(highlightbackground='#9c498c')
            self.oneButtonIsSelected = False
        else:
            buttenIds[self.firstSelectedButton].configure(highlightbackground='#e8e8e8')
            self.oneButtonIsSelected = False

    def firstSelectedButtonIsNotSecondSelectedButton(self, i, j):
        return not self.firstSelectedButton == self.getSelectedButton(i,j)

    def secondSelectedButtonIsNextToFirstSelectedButton(self, i, j):
        return False

    def getSelectedButton(self, i, j):
        return (i*9)+j

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