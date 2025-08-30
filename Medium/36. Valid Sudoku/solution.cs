public class Solution {
    public bool IsValidSudoku(char[][] board) {
        for(int i = 0; i < 10; i++){
            if(!IsValidRow(i, board) || !IsValidCol(i, board)) return false;
        }

        for(int i = 0; i < 9; i += 3){
            for(int j = 0; j < 9; j += 3){
                if(!IsValidUnit(i, j, board)) return false;
            }
        }

        return true;
    }

    public bool IsValidUnit(int x, int y, char[][] board) {
        int[] appear = new int[10];
        for(int i = x; i < x + 3; i++){
            for(int j = y; j < y + 3; j++){
                if(board[i][j] != '.'){
                    int num = board[i][j] - '0';
                    appear[num] += 1;
                    if(appear[num] != 1) return false;
                }
            }
        }

        return true;
    }

    public bool IsValidRow(int x, char[][] board) {
        int[] appear = new int[10];
        for(int i = 0; i < 9; i++){
            if(board[x][i] != '.'){
                int num = board[x][i] - '0';
                appear[num] += 1;
                if(appear[num] != 1) return false;
            }
        }

        return true;
    }

    public bool IsValidCol(int y, char[][] board) {
        int[] appear = new int[10];
        for(int i = 0; i < 9; i++){
            if(board[i][y] != '.'){
                int num = board[i][y] - '0';
                appear[num] += 1;
                if(appear[num] != 1) return false;
            }
        }

        return true;
    }
}