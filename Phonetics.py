from DictionaryOperations import DictionaryOperations
from LevenshteinDistance import LevenshteinDistance

class Phonetics:

    def __init__(self, _word):
        self.word = _word
        self.LevenshteinDistance = LevenshteinDistance()
        self.dictinary = DictionaryOperations("DATA/sozluk.txt")
        self.possibleRootList = {}
        self.responseList = []
        self.phoneticsControl()

    def phoneticsControl(self):
        lines = self.dictinary.getLines()
        for line in lines:
            selectedWords = line.split()[2] 
            flagWordsList = selectedWords.split("(")
            flagWords = ""
            if len(flagWordsList) > 1:
                flagWords = flagWordsList[1].split(")")[0]
            cost = self.LevenshteinDistance.LevenshteinCost(flagWords, self.word)

            if cost <= 10:
                self.possibleRootList[flagWords] = [line, cost]

        self.editPossibleRootList()

    def editPossibleRootList(self):
        values = self.possibleRootList.values()
        valuesCost = []
        for item in values:
            valuesCost.append(item[1])
        min_value = min(valuesCost)
        res = [key for key in self.possibleRootList if self.possibleRootList[key][1] == min_value]
        for item in res:
            self.responseList.append(self.possibleRootList[item][0])

    def getList(self):
        return self.responseList
