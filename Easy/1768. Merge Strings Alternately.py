class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ''
        for i in range(max(len(word1), len(word2))):
            res += word1[i] if i < len(word1) else ''
            res += word2[i] if i < len(word2) else ''
        return res
