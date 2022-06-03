from word_info import WordInfo
from DictionaryOperations import DictionaryOperations
from Suffixs import Suffixs
from Phonetics import Phonetics
from LevenshteinDistance import LevenshteinDistance
import random

class FiniteStateMachine:
    
    def __init__(self):
        #super().__init__(self)
        self.word = ""
        self.wordInfoList = []
        self.isPhonetics = False
        self.additinalFlag = False
        self.levenshteinFlag = False
        self.findLongWordFlag = False
        #self.WordInfo = WordInfo()
        possibleRootsOfWordCount = 0
        self.dictionaryFile = DictionaryOperations("DATA/sozluk.txt")
    
    def setWord(self, _word):
        self.word = _word
        possibleRootsOfWordCount = 0
        self.findPossibleRootsOfWord()
        if self.additinalFlag:
            self.splitAddition()
            return
        if ((len(self.wordInfoList) == 1) and (len(self.word) > 5)):
            self.findLongWordFlag = True
            self.findLongWord()
            return
        if (len(self.wordInfoList) == 1):
            self.levenshteinFlag = True
            self.changeWord()
        if not self.wordInfoList:
            self.isPhonetics = True
            possibleRootList = Phonetics(self.word).getList()
            for item in possibleRootList:
                self.addPossibleRootsOfWord(item)
        self.splitAddition()
        
    def findLongWord(self):
        linesList = self.dictionaryFile.likeOperator(self.word)
        self.addPossibleRootsOfWord(linesList[0])
        self.wordInfoList[0].setAdditionGroup(self.wordInfoList[0].getAdditionGroup())
        self.wordInfoList.pop(0)
        
    def changeWord(self):
        lines = self.dictionaryFile.getLines()
        lvnt = LevenshteinDistance()
        wordList = []
        sameLengthWordList = []
        for line in lines:
            selectedWord = line.split()[0]
            if line == self.word:
                continue
            cost = lvnt.LevenshteinCost(self.word, selectedWord)
            if cost == 1:
                wordList.append(line)
        for item in wordList:
            if len(self.word) == len(item.split()[0]):
                sameLengthWordList.append(item)
        result = sameLengthWordList[0]
        self.addPossibleRootsOfWord(result)
        self.wordInfoList[0].setAdditionGroup(self.wordInfoList[0].getAdditionGroup())
        self.wordInfoList.pop(0)

    def findPossibleRootsOfWord(self):
        tempWord = self.word
        while len(tempWord) >= 2:
            if self.dictionaryFile.wordFinder(tempWord):
                self.addPossibleRootsOfWord(self.dictionaryFile.getLine())

            tempWord = tempWord[:-1]

    def addPossibleRootsOfWord(self, _dictionaryLine):
        infoWord = WordInfo(_dictionaryLine)
        if infoWord.type == "fiil":
            return
        self.wordInfoList.append(infoWord)

    def splitAddition(self):
        for possibleRoot in self.wordInfoList:
            if self.isPhonetics:
                startIndex =  possibleRoot.flag.split("(")[1].split(")")[0]
                additionGroup = self.word[len(startIndex):]
            else:
                additionGroup = self.word[len(possibleRoot.root):]
            possibleRoot.setAdditionGroup(additionGroup)
            additionList = Suffixs(additionGroup).findSuffixs()
            possibleRoot.setAdditionsList(additionList)
        
    def getInfo(self):
        return self.wordInfoList