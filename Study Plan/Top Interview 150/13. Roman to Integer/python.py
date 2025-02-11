class Solution:
    def romanToInt(self, s: str) -> int:
        romanValue = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        res = 0
        for i in range(len(s) - 1):
            if romanValue[s[i]] < romanValue[s[i + 1]]:
                res -= romanValue[s[i]]
            else:
                res += romanValue[s[i]]
        return res + romanValue[s[-1]]
