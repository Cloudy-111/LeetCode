class Solution:
    # nếu cả chuối là 1 số thì chỉ cần trả về độ dài - 1
    # vì đề yêu cầu không chia xâu rỗng nên không duyệt đến hết xâu
    def maxScore(self, s: str) -> int:
        if len(set(list(s))) == 1:
            return len(s) - 1
        left, right = 0, s.count('1')
        res = 0
        for i in range(len(s) - 1):
            if s[i] == '0':
                left += 1
            if s[i] == '1':
                right -= 1
            res = max(res, left + right)
        return res
