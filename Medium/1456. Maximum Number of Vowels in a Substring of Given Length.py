class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = 'aiueo'
        tmp = 0
        for i in range(k):
            if s[i] in vowel:
                tmp += 1
        res = tmp
        for i in range(k, len(s)):
            if s[i] in vowel:
                tmp += 1
            if s[i - k] in vowel:
                tmp -= 1
            res = max(res, tmp)
        return res
