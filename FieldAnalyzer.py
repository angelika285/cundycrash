from FieldFiller import FieldFiller

class FieldAnalyzer:

    def __init__(self, field, pointsInstanz, buttonIds):
        self.field = field
        self.pointsInstanz = pointsInstanz
        self.fieldFiller = FieldFiller(self.field, buttonIds)

    def checkRow(self):
        for row in range(0, self.field.shape[0]):
            for column in range(0, self.field.shape[1]-2):
                self.pointsInstanz.setEarnedPoints(self.checkItemInRow(row, column))
        #self.updateScoreLabel()

    def checkItemInRow(self, row, column):
        sameValue = 1
        # TODO: bei gefundenem paar reihe von neu beginnen
        while column < 8 and self.field[row][column] == self.field[row][column+1]:
            sameValue += 1
            column += 1
        if sameValue > 2:
            self.fieldFiller.changeRowFieldValues(sameValue ,row, column-sameValue+1)
        return sameValue

    def checkColumn(self):
        for row in reversed(range(0+2, self.field.shape[0])):
            for column in range(0, self.field.shape[1]):
                self.pointsInstanz.setEarnedPoints(self.checkItemInColumn(row, column))
                column += 1
        #self.updateScoreLabel()

    def checkItemInColumn(self, row, column):
        # TODO: bei gefundenem paar zeile von neu beginnen
        sameValue = 1
        while row > 0 and self.field[row][column] == self.field[row-1][column]:
            sameValue += 1
            row -= 1
        if sameValue > 2:
            self.fieldFiller.changeColumnFieldValues(sameValue, row+sameValue, column)
        return sameValue