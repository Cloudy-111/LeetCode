class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        lst = text.split()
        res = len(lst)
        for i in lst:
            for char in brokenLetters:
                if char in i:
                    res -= 1
                    break
        return res
