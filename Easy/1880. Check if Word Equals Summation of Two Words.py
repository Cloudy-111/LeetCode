class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def toNum(s):
            res = 0
            for i in s:
                res = res * 10 + ord(i) - ord('a')
            return res

        first = toNum(firstWord)
        second = toNum(secondWord)
        target = toNum(targetWord)
        return first + second == target
