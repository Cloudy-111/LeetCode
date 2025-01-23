class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0
        for i in range(m):
            s = sum(grid[i])
            if s > 1:
                res += s
            elif s == 1:
                col = grid[i].index(1)
                if sum(grid[row][col] for row in range(m)) > 1:
                    res += 1
        return res