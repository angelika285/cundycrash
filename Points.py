class Points:
    
    def __init__(self):
        self.points = 0

    def setEarnedPoints(self, sameValues):
        self.points += self.checkForEarnedPoints(sameValues)

    def checkForEarnedPoints(self, sameValues):
        if sameValues == 3:
            return 10
        elif sameValues == 4:
            return 20
        elif sameValues == 5:
            return 30
        elif sameValues == 6:
            return 40
        elif sameValues == 7:
            return 50
        elif sameValues == 8:
            return 60
        elif sameValues == 9:
            return 70
        elif sameValues == 10:
            return 80
        else:
            return 0