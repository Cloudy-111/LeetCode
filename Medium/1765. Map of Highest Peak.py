from collections import deque


class Solution:
    # Sử dụng BFS để tìm khoảng cách từ các ô chứa nước đến các ô không chứa nước, BFS từ nhiều nguồn
    # Đánh dấu các ô chứa nước và thêm vào queue, dần dần lan qua các ô xung quanh(những ô chưa đặt height) với height[ni][nj] = height[i][j] + 1
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        height = [[-1] * n for _ in range(m)]
        queue = deque()

        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    height[i][j] = 0
                    queue.append((i, j))

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            i, j = queue.popleft()
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and height[ni][nj] == -1:
                    height[ni][nj] = height[i][j] + 1
                    queue.append((ni, nj))

        return height
