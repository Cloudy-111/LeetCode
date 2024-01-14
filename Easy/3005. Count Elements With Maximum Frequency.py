class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        dic = Counter(nums)
        res, peak = 0, 0
        for i in dic:
            if dic[i] > peak:
                peak = dic[i]
        for i in dic:
            if dic[i] == peak:
                res += dic[i]
        return res
