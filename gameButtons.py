import random
import numpy as np

class GameButtons:
    numberOfRows = 9
    numberOfColumns = 10
    field = None

    def __init__(self):
        self.field = np.random.randint(6, size=(self.numberOfColumns, self.numberOfRows))
        self.checkForRightInitializedRow()
        self.checkForRightInitializedColumn()
    
    def getFields(self):
        return self.field

    def getField(self, col, row):
        return self.field[col, row]

    def checkForRightInitializedRow(self):
        for row in range(0, self.field.shape[0]):
            for column in range(0, self.field.shape[1]-2):
                while self.field[row][column] == self.field[row][column+1] and self.field[row][column] == self.field[row][column+2]:
                    self.field[row][column+2] = random.randint(0, 6)

    def checkForRightInitializedColumn(self):
        for row in range(0, self.field.shape[0]-2):
            for column in range(0, self.field.shape[1]):
                while self.field[row][column] == self.field[row+1][column] and self.field[row][column] == self.field[row+2][column]:
                    self.field[row+2][column] = random.randint(0, 6)
