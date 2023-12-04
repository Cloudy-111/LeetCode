class Solution:
    def largestGoodInteger(self, num: str) -> str:
        num += '.'
        res = '0'
        cnt = 1
        chk = 0
        for i in range(1, len(num)):
            if num[i] != num[i - 1]:
                if cnt >= 3:
                    res = max(res, num[i - 1])
                    chk = 1
                cnt = 1
            else:
                cnt += 1
        if chk == 0:
            return ''
        return res * 3
