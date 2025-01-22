from collections import deque


class Solution:
    # Sử dụng BFS để tìm được đường ra ngắn nhất từ entrance
    # Đánh dấu các ô đã đi qua bằng ký tự "+" để không quay lại ô đã đi
    # Khi nào pop hết các phần tử trong queue ở trạng thái trước thì tăng biến step lên 1
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        queue = deque()
        queue.append((entrance[0], entrance[1]))
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        step = 0

        l = len(queue)  # lưu độ dài của queue trạng thái trước
        maze[entrance[0]][entrance[1]] = "+"
        while queue:
            if l == 0:
                l = len(queue)
                step += 1
            i, j = queue.popleft()
            l -= 1
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and maze[ni][nj] != "+":
                    maze[ni][nj] = "+"
                    # Nếu bước tiếp theo là biên thì trả về step + 1
                    if ni == 0 or ni == m - 1 or nj == 0 or nj == n - 1:
                        return step + 1
                    queue.append((ni, nj))
        return -1
