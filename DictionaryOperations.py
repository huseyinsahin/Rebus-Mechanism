class DictionaryOperations:

    def __init__(self, _fileName):
        self.fileRowsCount = 0
        self.fileName = _fileName
        self.lineList = []

    def fileOpen(self):
        try:
            self.dictionary = open(self.fileName,'r', encoding = 'utf-8')
        except:
            raise Exception("HATA")

    def setFileName(self, _fileName):
        self.fileName = _fileName
    
    def getFileName(self):
        return self.fileName
    
    def getFileRowsCounter(self):
        self.fileOpen()
        line_count = 0
        for line in self.dictionary:
            if line != "\n":
                line_count += 1
        self.fileClose()
        return line_count
    
    def wordFinder(self, _searchedWord):
        self.fileOpen()
        for line in self.dictionary:
           word = line.split()[0]
           if _searchedWord == word:
               self.line = line
               self.fileClose()
               return True

        self.fileClose()
        return False
        
    def likeOperator(self, _enteredWord):
        self.fileOpen()
        for line in self.dictionary:
           word = line.split()[0]
           if _enteredWord == word:
               continue
           if _enteredWord in word:
               self.lineList.append(line)

        self.fileClose()
        return self.lineList

    def getLines(self):
        self.fileOpen()
        lines = self.dictionary.readlines()
        self.fileClose()
        return lines

    def getSes(self):
        self.fileOpen()
        counter = 0
        for line in self.dictionary:
            flag = line.split()[2]
            if flag != "0":
                counter += 1
        self.fileClose()
    
    def fileClose(self):
        self.dictionary.close()
    
    def getLine(self):
        return self.line
    