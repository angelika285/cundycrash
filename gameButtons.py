from random import*

class gameButtons:
    numberOfFields = 9
    field = None

    def __init__(self):
        self.field =[[randint(0,4) for x in range(self.numberOfFields)] for y in range(self.numberOfFields)]
    
    def getField(self):
        return self.field
