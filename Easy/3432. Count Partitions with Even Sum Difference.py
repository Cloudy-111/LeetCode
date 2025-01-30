class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        pref = [0]
        n = len(nums)
        for i in range(n):
            pref.append(pref[-1] + nums[i])
        res = 0
        for i in range(1, n):
            left = pref[i]
            right = pref[n] - pref[i]
            if (abs(left - right) % 2 == 0):
                res += 1
        return res
