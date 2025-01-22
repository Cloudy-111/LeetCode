from collections import deque


class Solution:
    # Tương tự như bài 1765. Map of Highest Peak
    # Sử dụng BFS để tìm khoảng cách từ các ô = 0 đến các ô = 1, BFS từ nhiều nguồn
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        height = [[0] * n for _ in range(m)]
        queue = deque()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    height[i][j] = -1
                else:
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
