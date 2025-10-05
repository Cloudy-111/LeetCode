class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n, m = len(heights), len(heights[0])
        can_in_Pacific = [[0] * m for _ in range(n)]
        can_in_Atlantis = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0: can_in_Pacific[i][j] = 1
                if i == n - 1 or j == m - 1: can_in_Atlantis[i][j] = 1
        
        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0:
                    self.BFS(can_in_Pacific, i, j, heights)
                if i == n - 1 or j == m - 1:
                    self.BFS(can_in_Atlantis, i, j, heights)

        # self.printMatrix(can_in_Pacific)
        # print()
        # self.printMatrix(can_in_Atlantis)

        res = []
        for i in range(n):
            for j in range(m):
                if can_in_Pacific[i][j] == 1 and can_in_Atlantis[i][j] == 1:
                    res.append([i, j])
        
        return res
    
    def BFS(self, matrix, i, j, heights):
        moveX = [-1, 0, 1, 0]
        moveY = [0, -1, 0, 1]
        n, m = len(matrix), len(matrix[0])

        queue = []
        queue.append([i, j])

        while queue:
            x, y = queue.pop(0)
            for k in range(4):
                newX = x + moveX[k]
                newY = y + moveY[k]

                if 0 <= newX < n and 0 <= newY < m and matrix[newX][newY] == 0:
                    if heights[x][y] <= heights[newX][newY]:
                        queue.append([newX, newY])
                        matrix[newX][newY] = 1

    # def printMatrix(self, matrix):
    #     for i in range(len(matrix)):
    #         for j in range(len(matrix[0])):
    #             print(matrix[i][j], end=' ')
    #         print("")