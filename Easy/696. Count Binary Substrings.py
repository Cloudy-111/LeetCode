class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        lst = []
        if s[-1] == '0':
            s += '1'
        else:
            s += '0'
        cnt = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                cnt += 1
            else:
                lst.append(cnt)
                cnt = 1
        print(lst)
        res = 0
        for i in range(1, len(lst)):
            res += min(lst[i], lst[i - 1])
        return res
