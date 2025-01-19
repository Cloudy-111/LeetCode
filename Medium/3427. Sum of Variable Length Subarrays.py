class Solution:
    # Use prefix sum to calcaulate sum of subarray from start to i
    def subarraySum(self, nums: List[int]) -> int:
        pref = [0]
        start = []
        res = 0
        for i in range(len(nums)):
            pref.append(pref[-1] + nums[i])
            start.append(0 if i - nums[i] < 0 else i - nums[i])
        for i in range(len(start)):
            res += pref[i + 1] - pref[start[i]]
        return res
