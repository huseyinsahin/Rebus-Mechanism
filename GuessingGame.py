import random
from RebusGenerator import RebusGenerator

class GuessingGame:
    
    def __init__(self):
        self.allRebusWords = ["birikim", "gözlükçüler", "balıkesir", "karadeniz", "koltuk", "dolu", "kirpi", "ayet", "grafik", "burnu"]
        
    def getRebusImage(self):
        self.selectRebusWord = random.choice(self.allRebusWords)
        #print(self.selectRebusWord)
        rebusGenerator = RebusGenerator()
        imageList = rebusGenerator.generat(self.selectRebusWord)
        return imageList
        
    def guessWordCompareToRebus(self, gamerWord):
        if gamerWord == self.selectRebusWord:
            return True
        else:
            return False
            
    def changeRebusImage(self):
        temporyRebusWordList = ["birikim", "gözlükçüler", "balıkesir", "karadeniz", "koltuk", "dolu", "kirpi", "ayet", "grafik"]
        temporyRebusWordList.remove(self.selectRebusWord)
        self.selectRebusWord = random.choice(temporyRebusWordList)
        rebusGenerator = RebusGenerator()
        imageList = rebusGenerator.generat(self.selectRebusWord)
        return imageList
    