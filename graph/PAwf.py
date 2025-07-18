# 417. Pacific Atlantic Water Flow (Medium)

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        pacific = set()
        atlantic = set()

        def dfs(r, c, visitedSet):
            if (r, c) in visitedSet:
                return
            
            visitedSet.add((r, c))
            
            for dr, dc in directions:
                newR, newC = r+dr, c+dc
                if (0 <= newR < ROWS and 0 <= newC < COLS 
                and (newR, newC) not in visitedSet 
                and heights[newR][newC] >= heights[r][c]):
                    dfs(newR, newC, visitedSet)

        for c in range(COLS):
            dfs(0, c, pacific)
            dfs(ROWS-1, c, atlantic)

        for r in range(ROWS):
            dfs(r, 0, pacific)
            dfs(r, COLS-1, atlantic)
        
        shared = pacific.intersection(atlantic)
        return [[r, c] for r, c in shared]