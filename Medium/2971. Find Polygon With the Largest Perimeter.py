class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums = sorted(nums)
        prefix = [0] * len(nums)
        prefix[0] = nums[0]
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] + nums[i]
        for i in range(2, len(nums)):
            if nums[i] >= prefix[i - 1]:
                if i > 2:
                    return prefix[i - 1]
        return -1
