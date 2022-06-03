from FiniteStateMachine import FiniteStateMachine
from DatabaseOperations import DatabaseOperations

import difflib

class RebusGenerator:
    def __init__(self):
        self.diffList = []
        self.allRebusWords = ["birikim", "gözlükçüler", "balıkesir", "karadeniz", "koltuk", "dolu", "kirpi", "ayet", "grafik", "piton" ,"burnu"]
        
    def generat(self, _word):
        if not _word in self.allRebusWords:
            return []
        self.levenshteinFlag = False
        self.findLongWordFlag = False
        self.word = _word.lower()
        self.fsm = FiniteStateMachine()
        self.fsm.setWord(self.word)
        self.infoList = self.fsm.getInfo()
        self.dbOp = DatabaseOperations()
        self.rebusWords = []
        if self.fsm.findLongWordFlag:
            self.findLongWordFlag = True
            self.rebusWords.append(self.infoList[0].root)
            self.splitFindLongWord(self.infoList[0].root)
            return self.getImages()
        if not self.fsm.levenshteinFlag:
            if self.objectListLength(self.infoList) > 1:
                if len(self.infoList) >1:
                    self.detectRebusWords(self.infoList[1])
            else:
                self.rebusWords.append(self.infoList[0].root)
                self.rebusWords.append(self.infoList[0].additionGroup)
        else:
            self.levenshteinFlag = True
            self.rebusWords.append(self.infoList[0].root)
            self.diffLevenshteinWord()
       
        return self.getImages()
        
    def splitFindLongWord(self, usingWord):
        self.rebusWords.append("-")
        self.rebusWords.append(usingWord.split(self.word)[1])
        #print(self.rebusWords)
    
    def getDiffList(self):
       return self.diffList
       
    def diffLevenshteinWord(self):
        self.diffList.clear()
        for i,s in enumerate(difflib.ndiff(self.word, self.infoList[0].root)):
          if s[0]==' ': continue
          elif s[0]=='-':
            self.diffList.append(s[-1])

          elif s[0]=='+':
            self.diffList.append(s[-1])

    def detectRebusWords(self, gotInfoWord):
        self.rebusWords.append(gotInfoWord.root)
        additionGroup = gotInfoWord.getAdditionGroup()

        if additionGroup == "":
            return
        f = FiniteStateMachine()
        f.additinalFlag = True
        f.setWord(additionGroup)
        if not f.getInfo():
            self.rebusWords.append(additionGroup)
            return
        self.detectRebusWords(f.getInfo()[0])

    def objectListLength(self, infoList):
        length = 0
        for i in infoList:
            length += 1
        return length

    def getImages(self):
        images = []
        for item in self.rebusWords:
            image = self.dbOp.getImagePathByWord(item)
            if image != None:
                images.append(image)
            else:
                images.append(item)
        return images
