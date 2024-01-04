class Solution:
    # chỉ cần 1 dict lưu trữ vị trí của từng kí tự trong xâu
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        res = -1
        dic = {}
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = i
            else:
                res = max(res, i - dic[s[i]] - 1)
        return res
