class Solution:
    def maxScore(self, s: str) -> int:
        left = 1 if s[0] == '0' else 0
        right = s[1:].count('1')
        res = left + right
        for i in range(1, len(s) - 1):
            if s[i] == '1':
                right -= 1
                res = max(res, left + right)
            else:
                left += 1
                res = max(res, left + right)
        return res
