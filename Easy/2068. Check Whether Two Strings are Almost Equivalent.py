class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        def calDict(word):
            dic = defaultdict(int)
            for i in word:
                dic[i] += 1
            return dic
        dic1 = calDict(word1)
        dic2 = calDict(word2)
        s = set(word1 + word2)
        for i in s:
            if abs(dic1[i] - dic2[i]) > 3:
                return False
        return True
