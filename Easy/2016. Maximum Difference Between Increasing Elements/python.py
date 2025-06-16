class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        res = 0
        max_value = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            max_value = max(max_value, nums[i])
            if nums[i] < nums[i + 1]:
                res = max(res, max_value - nums[i])
        return res if res > 0 else -1