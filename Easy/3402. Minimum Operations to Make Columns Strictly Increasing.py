class Solution:
    # Chỉ cần duyệt từng cột một, nếu giá trị của hàng dưới nhỏ hơn bằng hàng trên thì cộng kết quả với sự chênh lệch giữa hàng trên + 1 và hàng dưới
    # Cập nhật lại giá trị của hàng dưới
    def minimumOperations(self, grid: List[List[int]]) -> int:
        res = 0
        amount = len(grid)
        if amount == 1:
            return 0
        for i in range(len(grid[0])):
            for j in range(1, len(grid)):
                if grid[j][i] <= grid[j - 1][i]:
                    res += grid[j - 1][i] + 1 - grid[j][i]
                    grid[j][i] = grid[j - 1][i] + 1
        return res
