from enum import Enum

class Images(Enum):
    ANDROIDSTUDIO = 0, "img/androidstudio.png"
    JAVA = 1, "img/java.png"
    JETBRAINS = 2, "img/jetbrains.png"
    PYTHON = 3, "img/python.png"
    VSC = 4, "img/vsc.png"
    JS = 5, "img/js.png"
    
    def __new__(cls, *args, **kwds):
        obj = object.__new__(cls)
        obj._value_ = args[0]
        return obj

    def __init__(self, number, path):
        self.number = number
        self.path = path

    def getNumber(self):
        return self.number

    def getPath(self):
        return self.path