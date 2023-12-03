from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        if set(word1) != set(word2):
            return False
        dic1 = Counter(word1)
        dic2 = Counter(word2)
        lst1, lst2 = [], []
        for i in dic1:
            lst1.append(dic1[i])
        for i in dic2:
            lst2.append(dic2[i])
        return lst1.sort() == lst2.sort()
