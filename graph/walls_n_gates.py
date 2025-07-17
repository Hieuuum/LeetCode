# 286. Walls and Gates (Medium)

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2147483647
        q = collections.deque()
        visited = set()

        def addCell(r, c):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS 
                or grid[r][c] == -1 or (r, c) in visited):
                return
            q.append((r, c))
            visited.add((r, c))
            
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        dist = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = min(dist, grid[r][c])
                for dr, dc in directions:
                    addCell(r+dr, c+dc)
            dist += 1