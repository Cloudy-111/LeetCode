class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * len(nums)
        curr = 0
        for i in range(1, len(nums)):
            if curr + nums[curr] >= i:
                dp[i] = dp[curr] + 1
            else:
                while curr < i and curr + nums[curr] < i:
                    curr += 1
                if dp[curr] != 0:
                    dp[i] = dp[curr] + 1
        return dp[n - 1]
