# 200. Number of Islands (Medium)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        count = 0
        
        def dfs(r, c):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS 
                or grid[r][c] == "0"):
                return
            
            grid[r][c] = "0"
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    count += 1
                    dfs(r, c)
        
        return count

