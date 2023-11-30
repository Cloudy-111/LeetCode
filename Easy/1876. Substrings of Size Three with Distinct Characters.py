class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s) - 3):
            st = set(s[i: i + 3])
            if len(st) == 3:
                res += 1
        return res
