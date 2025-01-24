class Solution:
    # Từ đề bài, ta có thể suy ra node an toàn là node không nằm trong chu trình và nối đến một node an toàn khác -> dùng đệ quy với các đỉnh kề với đỉnh hiện tại
    # https://leetcode.com/problems/find-eventual-safe-states/solutions/6322670/dfs-recursive-with-example-visual-by-clo-y2vx/
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        state = [0] * n  # 0: chưa thăm, 1: đang thăm, 2: an toàn

        def dfs(node):
            if state[node] != 0:  # Đã được xử lý
                return state[node] == 2
            state[node] = 1  # Đánh dấu đang thăm
            for neighbor in graph[node]:
                # Phát hiện chu trình hoặc node không an toàn
                if state[neighbor] == 1 or not dfs(neighbor):
                    return False
            state[node] = 2  # Đánh dấu là an toàn
            return True

        res = [node for node in range(n) if dfs(node)]

        res.sort()
        return res
