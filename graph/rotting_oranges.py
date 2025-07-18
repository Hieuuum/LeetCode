# 994. Rotting Oranges (Medium)

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        q = collections.deque()

        fresh = 0
        #append all rotten fruits
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        time = 0
        #use a queue
        while fresh > 0 and q:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    r_new, c_new = r+dr, c+dc
                    if (0 <= r_new < ROWS and 0 <= c_new < COLS 
                        and grid[r_new][c_new] == 1):
                        grid[r_new][c_new] = 2
                        q.append((r_new, c_new))
                        fresh -= 1

            time += 1

        #after stack empty check
        return time if fresh == 0 else -1