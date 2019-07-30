from FieldFiller import FieldFiller

class FieldAnalyzer:

    def __init__(self, field, pointsInstanz, buttonIds):
        self.field = field
        self.pointsInstanz = pointsInstanz
        self.fieldFiller = FieldFiller(self.field, buttonIds)
        self.foundFields = False
        self.foundMoreThanOne = False

    def checkField(self):
        self.foundFields = True
        while self.foundFields == True:
            self.foundFields = False
            self.checkRow()
            self.checkColumn()
        return self.foundMoreThanOne

    def checkRow(self):
        for row in range(0, self.field.shape[0]):
            for column in range(0, self.field.shape[1]-2):
                self.pointsInstanz.setEarnedPoints(self.checkItemInRow(row, column))

    def checkItemInRow(self, row, column):
        sameValue = 1
        while column < 8 and self.field[row][column] == self.field[row][column+1]:
            sameValue += 1
            column += 1
        if sameValue > 2:
            self.fieldFiller.changeRowFieldValues(sameValue ,row, column-sameValue+1)
            self.foundFields = True
            self.foundMoreThanOne = True
        return sameValue

    def checkColumn(self):
        for row in reversed(range(0+2, self.field.shape[0])):
            for column in range(0, self.field.shape[1]):
                self.pointsInstanz.setEarnedPoints(self.checkItemInColumn(row, column))
                column += 1

    def checkItemInColumn(self, row, column):
        sameValue = 1
        while row > 0 and self.field[row][column] == self.field[row-1][column]:
            sameValue += 1
            row -= 1
        if sameValue > 2:
            self.fieldFiller.changeColumnFieldValues(sameValue, row+sameValue, column)
            self.foundFields = True
            self.foundMoreThanOne = True
        return sameValue