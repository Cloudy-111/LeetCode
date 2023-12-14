class Solution:
    # Cách 1: Brute Force, duyệt mảng tổng cột, tổng hàng, mỗi lần 1 for
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        row = []
        col = []
        for i in grid:
            numOf1 = sum(i)
            row.appned((numOf1, len(i) - numOf1))
        for i in list(zip(*grid)):
            numOf1 = sum(i)
            col.append((numOf1, len(i) - numOf1))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] = row[i][0] + col[i][0] - row[i][1] - col[i][1]
        return grid

    # Cách 2: Lược đi 1 for
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        row, col = len(grid), len(grid[0])
        numsRow = [0] * row
        numsCol = [0] * col
        for i in range(row):
            for j in range(col):
                numsRow[i] += grid[i][j]
                numsCol[j] += grid[i][j]

        for i in range(row):
            for j in range(col):
                grid[i][j] = numsRow[i] + numsCol[j] - \
                    (row - numsRow[i]) - (col - numsCol[j])
        return grid
