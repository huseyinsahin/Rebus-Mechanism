class Suffixs:

    def __init__(self, _additionalGroup):
        self.additionalGroup = _additionalGroup
        self.additionalGroupContainsSuffixs = []
        self.suffixs = {
            "Yapım Ekleri": ["inci", "uncu", "üncü", "lik", "luk", "lık", "lük", "siz", "sız", "suz",
                                                "süz", "cak", "cek", "cık", "cik", "cuk", "cük", "çık", "çik", "çuk",
                                                "çük", "cal", "cel", "cıl", "cil", "cul", "cül", "çıl", "çil", "çul",
                                                "çül", "daş", "deş", "taş", "teş", "msı", "msi", "sal", "sel", "sıl",
                                                "sil", "sul", "sül", "çü", "la", "le", "lı", "li", "lu", "lü", "ıt",
                                                "it", "ut", "üt", "at", "et", "tı", "ti", "tu", "tü","cu"],
            "Bulunma Durumu Eki": ["da", "de", "ta", "te"],
            "Çokluk Eki": ["lar", "ler"],
            "Ayrılma Durumu Eki": ["den", "dan", "ten", "tan"],
            "İlgi Eki": ["ın", "in", "un", "ün"],
            "İyelik Eki": ["miz", "niz", "leri"],
            "Eşitlik Eki": ["ca", "ce", "ça", "çe"]}


    def findSuffixs(self):
        start = -1 * len(self.additionalGroup) - 1
        end = -1
        find = True
        self.additionalGroup += '.'

        while find:
            find = False
            for suffix in self.suffixs.keys():
                for i in range(start, end):
                    if self.additionalGroup[i:end] in self.suffixs[suffix]:

                        self.additionalGroupContainsSuffixs.append(self.additionalGroup[i:end])
                        find = True
                        end = i
                        break
        self.reversList()
        return self.additionalGroupContainsSuffixs

    def reversList(self):
        self.additionalGroupContainsSuffixs.reverse()


obj = Suffixs("luculuk.")
obj.findSuffixs()
