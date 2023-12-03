class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = 0
        acc = 0
        for i in range(len(gain)):
            acc += gain[i]
            res = max(res, acc)
        return res
