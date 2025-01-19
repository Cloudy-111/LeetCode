class Solution:
    # Sử dụng quy hoạch động, với dp[i][j][k] là kết quả tối ưu thu được tại hàng i, cột j và vô hiệu hóa k tên trộm
    # Khi duyệt đến hàng i, cột j số tiền tối ưu sẽ là max(top, left) là kết quả trước khi đến ô đó, cộng thêm số tiền tại coins[i][j]
    # Nếu coins[i][j] mà âm tức là ở ô đó có trộm, robot sẽ thực hiện tối ưu(vô hiệu hóa tên trộm hoặc không) = max giữa bị trộm hoặc vô hiệu hóa trộm và không mất tiền
    # Cuối cùng, ta sẽ so sánh và lấy max của các trường hợp: vô hiệu hóa 1, vô hiệu hóa 2 và không vô hiệu hóa
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])
        dp = [[[float('-inf')] * 3 for _ in range(n)] for _ in range(m)]
        dp[0][0][0] = coins[0][0]

        if coins[0][0] < 0:
            dp[0][0][1] = 0

        for i in range(m):
            for j in range(n):
                for k in range(3):
                    if i == 0 and j == 0:
                        continue

                    top = dp[i - 1][j][k] if i > 0 else float('-inf')
                    left = dp[i][j - 1][k] if j > 0 else float('-inf')
                    current = max(top, left)

                    dp[i][j][k] = current + coins[i][j]

                    if coins[i][j] < 0 and k > 0:
                        neutralized_top = dp[i-1][j][k -
                                                     1] if i > 0 else float('-inf')
                        neutralized_left = dp[i][j-1][k -
                                                      1] if j > 0 else float('-inf')
                        dp[i][j][k] = max(dp[i][j][k], max(
                            neutralized_top, neutralized_left))

        return max(dp[m - 1][n - 1][0], dp[m - 1][n - 1][1], dp[m - 1][n - 1][2])
