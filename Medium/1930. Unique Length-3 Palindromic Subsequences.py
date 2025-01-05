class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        d = {}
        for i, char in enumerate(s):
            if char in d:
                d[char] = max(d[char], i)
            else:
                d[char] = i
        res = 0
        seen = set()
        for i in range(len(s)):
            if s[i] not in seen and d[s[i]] != i:
                seen.add(s[i])
                # print(s[i], s[i + 1 : d[s[i]]])
                res += len(set(s[i + 1 : d[s[i]]]))
        return res