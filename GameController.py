class GameController:
    
    def __init__(self, scoreLabel, field):
        self.points = 0
        self.scoreLabel = scoreLabel
        self.field = field
        self.oneButtonIsSelected = False

    def buttonClicked(self, i, j, buttenIds):
        if not self.oneButtonIsSelected:
            buttenIds[(i*9)+j].configure(highlightbackground='#3E4149')
            self.oneButtonIsSelected = True
        else:
            buttenIds[(i*9)+j].configure(highlightbackground='#9c498c')
            self.oneButtonIsSelected = False

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