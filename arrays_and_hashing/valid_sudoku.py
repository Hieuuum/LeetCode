#36. Valid Sudoku (Medium)

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # No hints
        row = [[0 for _ in range(9)] for _ in range(9)]
        col = [[0 for _ in range(9)] for _ in range(9)]
        square = [[0 for _ in range(9)] for _ in range(9)]

        for i in range(9):
            for j in range(9):
                square_i = i//3*3 + j//3
                val = board[i][j]
                if not val.isdigit():
                    continue
                else:
                    val = int(val) - 1

                if square[square_i][val] == 1 or row[i][val] == 1 or col[val][j] == 1:
                    return False
                else:
                    square[square_i][val] = 1
                    row[i][val] = 1
                    col[val][j] = 1
        
        return True
