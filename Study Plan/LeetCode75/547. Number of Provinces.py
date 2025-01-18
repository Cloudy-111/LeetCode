class Solution:
    # Sử dụng thuật toán Union Find để tìm các cụm liên thông giữa các thành phố
    # Thêm rank để hợp nhất giữa 2 thành phố
    def __init__(self):
        self.parent = []
        self.rank = []

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.initialize(isConnected)
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1:
                    self.union_find(i, j)
        res = 0
        for i in range(len(isConnected)):
            if self.parent[i] == i:
                res += 1
        return res

    def initialize(self, isConnected):
        n = len(isConnected)
        self.parent = [0] * n
        self.rank = [0] * n
        for i in range(n):
            self.rank[i] = 0
            self.parent[i] = i

    def find_root(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find_root(self.parent[i])
        return self.parent[i]

    def union_find(self, i, j):
        root_i = self.find_root(i)
        root_j = self.find_root(j)
        if root_i != root_j:
            if self.rank[root_i] == self.rank[root_j]:
                self.parent[root_i] = root_j
                self.rank[root_j] += 1
            elif self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_i] = root_j
