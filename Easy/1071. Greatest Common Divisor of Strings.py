import math


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        m = min(len(str1), len(str2))
        s = str2 if m == len(str1) else str1
        for i in range(m):
            if str1[i] != str2[i]:
                return ''
        if str1 == str2:
            return str1
        x = math.gcd(len(str1), len(str2))

        def find(s, tmp):
            for i in range(1, len(s) // tmp):
                l = tmp * i
                if s[: l] * (len(s) // l) == s:
                    return s[: l]
            return ''
        return find(s, x)
