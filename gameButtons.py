from random import*
import numpy as np

class GameButtons:
    numberOfRows = 9
    numberOfColumns = 10
    field = None

    def __init__(self):
        self.field = np.random.randint(6, size=(self.numberOfColumns, self.numberOfRows))
    
    def getFields(self):
        return self.field
    
    def getField(self, col, row):
        return self.field[col, row]
