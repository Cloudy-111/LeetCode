class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >= k + maxPts:
            return 1.0

        dp = [0] * (n + maxPts + 1)
        for i in range(k, n + 1):
            dp[i] = 1.0

        windowSumProbability = sum(dp[k: k + maxPts])

        dp[k - 1] = windowSumProbability / maxPts
        for i in range(k - 2, -1, -1):
            windowSumProbability = windowSumProbability - \
                dp[i + maxPts + 1] + dp[i + 1]
            dp[i] = windowSumProbability / maxPts

        return dp[0]
