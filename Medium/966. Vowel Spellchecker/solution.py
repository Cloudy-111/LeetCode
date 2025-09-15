class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        words = set(wordlist)
        lower = {}
        pattern = {}

        for i in wordlist:
            wordlower = i.lower()
            if wordlower not in lower:
                lower[wordlower] = i

            patternword = self.pattern(i.lower())
            if patternword not in pattern:
                pattern[patternword] = i

        res = []
        for i in queries:
            if i in words:
                res.append(i)
            elif i.lower() in lower:
                res.append(lower[i.lower()])
            elif self.pattern(i.lower()) in pattern:
                res.append(pattern[self.pattern(i.lower())])
            else:
                res.append("")
        return res

    def pattern(self, word):
        return "".join("_" if i in "aiuoe" else i for i in word)
