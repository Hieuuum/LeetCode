# 1584. Min Cost to Connect Points (Medium)

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = {i: [] for i in range(N)}
        for i in range(len(points)-1):
            x1, y1 = points[i]
            for j in range(i, len(points)):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        
        minHeap = [[0, 0]]
        heapq.heapify(minHeap)
        visited = set()
        res = 0
        while len(visited) != N:
            cost, i = heapq.heappop(minHeap)
            if i in visited:
                continue
            res += cost
            visited.add(i)
            for neiCost, nei in adj[i]:
                if nei not in visited:
                    heapq.heappush(minHeap, [neiCost, nei])
            
        return res