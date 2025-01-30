class Solution:
    # Nếu có thể tô màu các đỉnh của đồ thị bằng hai màu sao cho không có hai đỉnh kề nhau có cùng màu, thì đồ thị đó là hai phía.
    # Sử dụng DFS để tô màu cho các đỉnh khi duyệt
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n
        stack = []

        for i in range(len(graph)):
            stack.append(i)
            while stack:
                node = stack.pop()
                for neighbor in graph[node]:
                    if color[neighbor] == -1:
                        color[neighbor] = 1 - color[node]
                        stack.append(neighbor)
                    elif color[neighbor] == color[node]:
                        return False
        return True

# Giảm số lần duyệt bằng cách chỉ duyệt qua những node chưa đươc tô màu


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n

        def dfs(node: int) -> bool:
            stack = [node]
            while stack:
                u = stack.pop()
                for v in graph[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        stack.append(v)
                    elif color[v] == color[u]:
                        return False
            return True

        for i in range(n):  # Duyệt qua các node, xử lý khi đồ thị không liên thông
            if color[i] == -1:
                color[i] = 0
                if not dfs(i):
                    return False
        return True
