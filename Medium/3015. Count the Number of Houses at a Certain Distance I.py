from collections import deque


class Solution:
    # vì n <= 100 nên cách này chạy được trong thời gian thỏa mãn
    # với mỗi nhà, BFS nó và + thêm vào mảng dis
    # còn n lên đến 10^5 thì thành mức khó
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        self.res = [0 for _ in range(n + 1)]
        self.adj = [[] for _ in range(n + 1)]
        self.visited = [0 for _ in range(n + 1)]
        for i in range(1, n + 1):
            if i == 1:
                self.adj[i].append(i + 1)
            elif i == n:
                self.adj[i].append(n - 1)
            else:
                self.adj[i].append(i - 1)
                self.adj[i].append(i + 1)
        self.adj[x].append(y)
        self.adj[y].append(x)
        for i in range(1, n + 1):
            print(i, self.adj[i])

        def BFS(start):
            q = deque()
            q.append([start, 0])
            self.visited[start] = 1
            while q:
                t, dis = q.popleft()
                self.res[dis] += 1
                for i in self.adj[t]:
                    if self.visited[i] == 0:
                        q.append([i, dis + 1])
                        self.visited[i] = 1
        for i in range(1, n + 1):
            self.visited = [0] * (n + 1)
            BFS(i)
        return self.res[1:]
