class WordInfo:
    def __init__(self, line):
        self.root = line.split()[0]
        self.type = line.split()[1]
        self.flag = line.split()[2]
        self.additionsList = []
        self.additionGroup = ""

    def setRoot(self, _root):
        self.root = _root
    
    def setType(self, _type):
        self.type = _type

    def setFlag(self, _flag):
        self.flag = _flag

    def setAdditionGroup(self, _additionGroup):
        self.additionGroup = _additionGroup

    def getAdditionGroup(self):
        return self.additionGroup
    
    def setAdditionsList(self, _additions):
        self.additionsList = _additions

    def getAdditionsList(self):
        return self.additionsList
