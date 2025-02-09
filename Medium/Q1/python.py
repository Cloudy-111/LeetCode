class Solution:
    # Vì n <= 10 nên brute force là được, đưa những phần tử trên đường chéo vào một mảng rồi sort lại
    # Sau đó đưa lại vào ma trận
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        res = [[0] * n for _ in range(n)]
        row = 0
        col = n - 1
        while col > 0:
            arr = []
            j = col
            i = row
            while j < n:
                arr.append(grid[i][j])
                j += 1
                i += 1
            arr.sort()
            j = col
            i = row
            k = 0
            while j < n:
                res[i][j] = arr[k]
                j += 1
                i += 1
                k += 1
            col -= 1
        while row < n:
            arr = []
            j = col
            i = row
            while i < n:
                arr.append(grid[i][j])
                i += 1
                j += 1
            arr.sort(reverse=True)
            j = col
            i = row
            k = 0
            while i < n:
                res[i][j] = arr[k]
                j += 1
                i += 1
                k += 1
            row += 1
        return res
