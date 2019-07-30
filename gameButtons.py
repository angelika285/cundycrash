import random
import numpy as np

class GameButtons:
    numberOfRows = 9
    numberOfColumns = 10
    field = None

    def initializeGameButtons(self):
        self.field = np.random.randint(6, size=(self.numberOfColumns, self.numberOfRows))
        self.checkForRightInitialization()
    
    def getFields(self):
        return self.field

    def getField(self, col, row):
        return self.field[col, row]

    def checkForRightInitialization(self):
        for row in range(0, self.field.shape[0]):
            for column in range(0, self.field.shape[1]):
                oldValue = None
                if column < self.field.shape[1]-2 and self.areThreeInARow(row, column):
                    oldValue = self.field[row][column]
                    self.checkRow(row, column)
                if row < self.field.shape[0]-2:
                    self.checkColumn(row, column, oldValue)

    def areThreeInARow(self, row, column):
        return self.field[row][column] == self.field[row][column+1] and self.field[row][column] == self.field[row][column+2]

    def checkRow(self, row, column):
        while self.field[row][column] == self.field[row][column+1] and self.field[row][column] == self.field[row][column+2]:
            self.fillFieldWithNewValue(row, column)

    def checkColumn(self, row, column, oldValue):
        while (self.field[row][column] == self.field[row+1][column] and self.field[row][column] == self.field[row+2][column]) or self.field[row][column] == oldValue:
            self.fillFieldWithNewValue(row, column)

    def fillFieldWithNewValue(self, row, column):
        self.field[row][column] = random.randint(0,5)

    