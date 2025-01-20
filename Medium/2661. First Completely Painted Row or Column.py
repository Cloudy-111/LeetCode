class Solution:
    # Để dòng hoặc cột được tô đầy có nghĩa là tổng các ô được tô(được tô đặt là 1) trong 1 hàng phải bằng số cột và trong 1 cột phải bằng số hàng
    # Dùng mảng col(len = n), row(len = m) với m, n là kích thước của ma trận để theo dõi xem hàng nào cột nào đầy đầu tiên
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        d = {}
        m = len(mat)
        n = len(mat[0])
        col = [0] * n
        row = [0] * m
        for i in range(m):
            for j in range(n):
                if mat[i][j] not in d:
                    d[mat[i][j]] = (i, j)
        for i in range(len(arr)):
            coor_row, coor_col = d[arr[i]]
            col[coor_col] += 1
            row[coor_row] += 1
            if col[coor_col] == m or row[coor_row] == n:
                return i
