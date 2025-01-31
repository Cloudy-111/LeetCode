from collections import deque
# https://leetcode.com/problems/making-a-large-island/solutions/6351521/bfs-dsu-with-detail-explanations-by-clou-eo4u/

# BFS
# Ý tưởng đầu tiên: từ mỗi số 0, ta thực hiện BFS để tìm ra kích thước của đảo lớn nhất mà nó có thể tạo ra
# Độ phức tạp: O(n^2 * BFS), duyệt qua mỗi phần tử quá nhiều lần nên sẽ bị TLE.


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        max_size = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def bfs(i, j):
            queue = deque()
            visit = set()
            queue.append((i, j))
            size = 0
            while queue:
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1 and (nx, ny) not in visit:
                        visit.add((nx, ny))
                        queue.append((nx, ny))
                        size += 1
            return size

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    max_size = max(max_size, bfs(i, j))
        return max_size if max_size else n * n

# Cần giảm số lần duyệt qua mỗi phần tử, ý tưởng: lưu kích thước của mỗi phần tử 1(thuộc 1 đảo) vào 1 dict, khi duyệt đến phần tử nào thì chỉ cần lấy ra kích thước của cả hòn đảo đó.
# Dùng DSU để lưu lại gốc của mỗi đảo, những phần tử thuộc cùng 1 đảo sẽ có cùng gốc, duyệt qua các phần tử 0, duyệt 4 hướng xung quanh nó và cộng các kích thước các đảo.


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:

        n = len(grid)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        parent = {}
        size = {}

        def initilize():
            for i in range(n):
                for j in range(n):
                    parent[(i, j)] = (i, j)
                    size[(i, j)] = 1

        def find_root(x):
            if parent[x] != x:
                parent[x] = find_root(parent[x])
            return parent[x]

        def union(x, y):
            root_x = find_root(x)
            root_y = find_root(y)
            if root_x != root_y:
                if size[root_x] > size[root_y]:
                    root_x, root_y = root_y, root_x
                parent[root_x] = root_y
                size[root_y] += size[root_x]

        initilize(grid)
        for i in range(n):  # gộp các phần tử 1 cùng nhau thành đảo
            for j in range(n):
                if grid[i][j] == 1:
                    for dx, dy in directions:
                        nx, ny = i + dx, j + dy
                        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
                            union((i, j), (nx, ny))

        island_size = {}
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    root = find_root((i, j))
                    island_size[root] = size[root]

        max_size = max(island_size.values(), default=0)

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:  # duyệt các phần tử 0
                    unique_roots = set()
                    for dx, dy in directions:  # duyệt 4 hướng xung quanh phần tử 0
                        nx, ny = i + dx, j + dy
                        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
                            unique_roots.add(find_root((nx, ny)))
                    sum_size = 1 + sum(island_size[root]
                                       for root in unique_roots)
                    max_size = max(max_size, sum_size)

        return max_size

# Cách làm DSU ở trên vẫn còn tốn nhiều bộ nhớ, mỗi lần tìm gốc thì lại phải duyệt qua nhiều lần, cần cải thiện hơn.
# Kết hợp ý tưởng "lưu kích thước đại diện mỗi đảo" và sử dụng BFS để tìm các đảo như cách đầu tiên.

# Đánh dấu id cho từng đảo, sử dụng lại mảng grid để theo dõi tiến trình duyệt đảo.
# Độ phức tạp: O(n^2) với n là kích thước của grid.


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        island_id = 2  # id của đảo, bắt đầu từ 2, tránh 0, 1 để phân biệt với phần tử 0, 1 trong grid
        island_size = {}  # lưu kích thước của mỗi đảo

        def bfs(i, j, id):  # có thể dùng BFS hoặc DFS ở đây
            queue = deque([(i, j)])
            grid[i][j] = id  # đánh dấu id cho phần tử đầu tiên
            size = 1

            while queue:
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = id
                        queue.append((nx, ny))
                        size += 1
            return size

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    island_size[island_id] = bfs(i, j, island_id)
                    island_id += 1

        if not island_size:
            return 1

        max_size = max(island_size.values())

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    unique_ids = set()
                    for dx, dy in directions:
                        nx, ny = i + dx, j + dy
                        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] != 0:
                            unique_ids.add(grid[nx][ny])
                    sum_size = 1 + sum(island_size[id] for id in unique_ids)
                    max_size = max(max_size, sum_size)
        return max_size
