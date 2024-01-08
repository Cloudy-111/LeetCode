class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        cur = int(current[:2]) * 60 + int(current[3:])
        cor = int(correct[:2]) * 60 + int(correct[3:])
        dur = cor - cur
        incr = [1, 5, 15, 60]
        res = 0
        for i in range(3, -1, -1):
            res += dur // incr[i]
            dur %= incr[i]
        return res
