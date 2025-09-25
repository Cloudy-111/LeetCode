class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n, m = len(triangle), len(triangle[-1])
        dp = [[0] * m for _ in range(n)]
        dp[0][0] = triangle[0][0]
        for i in range(1, n):
            for j in range(i + 1):
                if 0 < j < i:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1]
                                   [j - 1]) + triangle[i][j]
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] + triangle[i][j]
                elif j == i:
                    dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]

        res = dp[n - 1][0]
        for i in range(m):
            res = min(res, dp[n - 1][i])

        return res
