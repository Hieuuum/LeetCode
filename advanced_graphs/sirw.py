# 778. Swim in Rising Water (Hard)

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        visited = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        
        minHeap = [[grid[0][0], 0, 0]] # time/max height, r, c
        heapq.heapify(minHeap)
        while minHeap:
            t, r, c = heapq.heappop(minHeap)
            if r == ROWS-1 and c == COLS-1:
                return t
            
            for dr, dc in directions:
                newR, newC = r+dr, c+dc
                if (min(newR, newC) >= 0 and newR < ROWS 
                and newC < COLS and visited[newR][newC] == 0):
                    visited[r][c] = 1
                    heapq.heappush(minHeap, [max(grid[newR][newC], t), newR, newC])

        
