# 130. Surrounded Regions (Medium)

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        def findSafeOs(r, c):
            board[r][c] = 'S'

            for dr, dc in directions:
                newR, newC = r+dr, c+dc
                if (0 <= newR < ROWS and 0 <= newC < COLS 
                and board[newR][newC] == 'O'):
                    findSafeOs(newR, newC)
        
        for c in range(COLS):
            if board[0][c] == 'O':
                findSafeOs(0, c)
            if board[ROWS - 1][c] == 'O':
                findSafeOs(ROWS - 1, c)

        for r in range(ROWS):
            if board[r][0] == 'O':
                findSafeOs(r, 0)
            if board[r][COLS - 1] == 'O':
                findSafeOs(r, COLS - 1)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'S':
                    board[r][c] = 'O'
                else:
                    board[r][c] = 'X'