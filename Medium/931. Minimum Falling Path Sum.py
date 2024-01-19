class Solution:
    # Dùng phương pháp quy hoạch động, lưu những trạng thái tốt nhất đến ô đó
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[float('inf')] * n for _ in range(n)]
        res = float('inf')
        # Gọi đệ quy đến tận hàng cuối cùng để chọn ra số thỏa mãn rồi quay ngược trở lên
        # Cách này bị cái là 1 ô bị duyệt qua nhiều lần, gây ra thời gian chạy có thể khá lớn

        def minPathSum(mat, row, col, dp):
            if n == 1:
                return mat[row][col]
            if row == n - 1:
                return mat[row][col]
            if dp[row][col] != float('inf'):
                return dp[row][col]
            left, right = float('inf'), float('inf')
            if col > 0:
                left = minPathSum(mat, row + 1, col - 1, dp)
            straight = minPathSum(mat, row + 1, col, dp)
            if col < n - 1:
                right = minPathSum(mat, row + 1, col + 1, dp)
            dp[row][col] = min(left, right, straight) + mat[row][col]
            return dp[row][col]
        for i in range(n):
            res = min(res, minPathSum(matrix, 0, i, dp))
        return res

    # Với cách qhd như này, mỗi phtu chỉ được duyệt qua 1 lần, rút ngắn thời gian hơn
    # Lưu luôn giá trị thỏa mãn vào dp cho mỗi hàng
    # Cách này trực quan và dễ hiểu hơn
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = matrix[0]  # Khởi tạo dp
        for i in range(1, n):
            t = dp[:]  # dp cho hàng tiếp theo
            for j in range(n):
                # với mỗi ô trong 1 hàng, dp của nó sẽ là min của các tổng trước nó + ô đó
                if j == 0:
                    t[j] = matrix[i][j] + min(dp[j], dp[j + 1])
                elif j == n - 1:
                    t[j] = matrix[i][j] + min(dp[j - 1], dp[j])
                else:
                    t[j] = matrix[i][j] + min(dp[j - 1], dp[j], dp[j + 1])
            dp = t
        return min(dp)
