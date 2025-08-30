class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            if self.isValidRow(i, board) == False:
                return False
            if self.isValidCol(i, board) == False:
                return False

        for i in range(0, 7, 3):
            for j in range(0, 7, 3):
                if self.isValidUnit(i, j, board) == False:
                    return False

        return True

    def isValidUnit(self, x, y, board):
        appear = [0] * 10
        for i in range(x, x + 3):
            for j in range(y, y + 3):
                if board[i][j] != ".":
                    appear[int(board[i][j])] += 1
                    if appear[int(board[i][j])] != 1:
                        return False
        return True

    def isValidRow(self, x, board):
        appear = [0] * 10
        for i in range(9):
            if board[x][i] != ".":
                appear[int(board[x][i])] += 1
                if appear[int(board[x][i])] != 1:
                    return False
        return True

    def isValidCol(self, y, board):
        appear = [0] * 10
        for i in range(9):
            if board[i][y] != ".":
                appear[int(board[i][y])] += 1
                if appear[int(board[i][y])] != 1:
                    return False
        return True
