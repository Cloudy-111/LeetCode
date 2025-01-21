from collections import deque


class Solution:
    def addToAdj(self, center, adj_point, adj):
        if center not in adj:
            adj[center] = []
        if adj_point not in adj:
            adj[adj_point] = []
        adj[center].append(adj_point)
        adj[adj_point].append(center)

    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        adj = {}
        visit = set()
        m = len(maze)
        n = len(maze[0])
        for i in range(m):
            for j in range(n):
                if maze[i][j] == ".":
                    if (i, j) not in adj:
                        adj[(i, j)] = []
                    if i > 0 and maze[i - 1][j] != "+":
                        self.addToAdj((i, j), (i - 1, j), adj)
                    if i < m - 1 and maze[i + 1][j] != "+":
                        self.addToAdj((i, j), (i + 1, j), adj)
                    if j > 0 and maze[i][j - 1] != "+":
                        self.addToAdj((i, j), (i, j - 1), adj)
                    if j < n - 1 and maze[i][j + 1] != "+":
                        self.addToAdj((i, j), (i, j + 1), adj)

        if len(adj) == 0:
            return -1
        entrace_tup = (entrance[0], entrance[1])
        queue = deque([(entrace_tup, 0)])
        visit.add(entrace_tup)

        res = 10**9

        while queue:
            current, dis = queue.popleft()
            i, j = current
            if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                if dis != 0:
                    res = min(dis, res)
            for neighbor in adj[current]:
                if neighbor not in visit:
                    visit.add(neighbor)
                    queue.append((neighbor, dis + 1))

        return res if res != 10**9 else -1
