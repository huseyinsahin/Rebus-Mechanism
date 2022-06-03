class LevenshteinDistance:
    def LevenshteinCost(self, sourceWord, targetWord):
        self.fword = targetWord
        self.sword = sourceWord
        self.lenfword = len(self.fword)
        self.lensword = len(self.sword)
        self.minlen = min(self.lenfword, self.lensword)

        if self.fword == "":
            return self.lensword
        if self.sword == "":
            return self.lenfword

        self.fark = abs(self.lensword - self.lenfword)
        self.sonuc = 0
        self.sonucters = 0

        for i in range(1, self.minlen + 1):
            if self.fword[i - 1] == self.sword[i - 1]:
                self.sonuc = self.sonuc + 0
            else:
                self.sonuc = self.sonuc + 1

            if self.fword[-i] == self.sword[-i]:
                self.sonucters = self.sonucters + 0
            else:
                self.sonucters = self.sonucters + 1

        self.sonuc = min(self.sonuc, self.sonucters)
        self.sonuc = self.sonuc + self.fark
        return self.sonuc
