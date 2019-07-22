from random import*
import numpy as np

class gameButtons:
    numberOfFields = 9
    field = None

    def __init__(self):
        self.field = np.random.randint(5, size=(self.numberOfFields, self.numberOfFields))
    
    def getField(self):
        return self.field
