from collections import deque


class Solution:
    # Sử dụng BFS để lan truyền nhiễm của cam, kết thúc khi không còn quả cam tươi nào để nhiễm
    # Nếu còn cam tươi thì trả về -1
    # Đưa các quả cam thối vào queue, lan truyền dần dần ra các quả xung quanh, khi nào queue trạng thái trước pop hết thì tăng biến res lên 1
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque()
        freshes = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    freshes += 1
        if freshes == 0:
            return 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        res = 1
        l = len(queue)  # lưu độ dài của queue trạng thái trước
        while queue:
            if l == 0:
                l = len(queue)
                res += 1
            i, j = queue.popleft()
            l -= 1
            for di, dj in directions:
                ni, nj = i + di, j + dj
                # Nếu là quả cam tươi, nhiễm thành quả cam thối và đưa vào queue
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                    freshes -= 1
                    grid[ni][nj] = 2
                    queue.append((ni, nj))
            if freshes == 0:
                break
        return res if freshes == 0 else -1
