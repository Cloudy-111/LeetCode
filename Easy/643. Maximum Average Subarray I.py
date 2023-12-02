class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        tmp = 0
        for i in range(k):
            tmp += nums[i]
        res = tmp / k
        for i in range(k, len(nums)):
            tmp -= nums[i - k]
            tmp += nums[i]
            res = max(res, tmp / k)
        return res
