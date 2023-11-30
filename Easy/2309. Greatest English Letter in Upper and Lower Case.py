class Solution:
    def greatestLetter(self, s: str) -> str:
        low = set(s.upper())
        res = ''
        for i in low:
            if i in s and i.lower() in s:
                if res > i:
                    res = i
        return res
