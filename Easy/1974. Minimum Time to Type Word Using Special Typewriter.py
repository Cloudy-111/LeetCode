class Solution:
    def minTimeToType(self, word: str) -> int:
        idx = 'a'
        res = 0
        for i in word:
            diff = abs(ord(i) - ord(idx))
            res += min(26 - diff, diff) + 1
            idx = i
        return res
