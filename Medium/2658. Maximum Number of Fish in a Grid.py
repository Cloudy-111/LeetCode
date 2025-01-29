class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        parent = {}
        res = {}

        def initilize(grid):
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    parent[(i, j)] = (i, j)

        def find_root(x):
            if parent[x] != x:
                parent[x] = find_root(parent[x])
            return parent[x]

        def union(x, y):
            root_x = find_root(x)
            root_y = find_root(y)
            if root_x != root_y:
                parent[root_y] = root_x

        initilize(grid)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                for dx, dy in directions:
                    x, y = i + dx, j + dy
                    if 0 <= x < m and 0 <= y < n and grid[x][y] != 0:
                        union((i, j), (x, y))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                root = find_root((i, j))
                if root not in res:
                    res[root] = 0
                res[root] += grid[i][j]
        return max(res.values()) if len(res) > 0 else 0
