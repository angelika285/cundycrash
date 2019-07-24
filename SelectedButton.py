class SelectedButton:

    def __init__(self, row, column, buttonIds):
        self.row = row
        self.column = column
        self.buttonIds = buttonIds
        self.button = self.getSelectedButton(self.getSelectedButtonIndex(row, column))

    def getSelectedButtonIndex(self, row, column):
        return (row*9)+column
    
    def getSelectedButton(self, index):
        return self.buttonIds[index]