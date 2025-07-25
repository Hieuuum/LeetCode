# 743. Network Delay Time (Medium)

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i: [] for i in range(1, n+1)}
        
        for start, end, time in times:
            adj[start].append([end, time])
        
        visited = set()
        minHeap = [[0, k]]
        heapq.heapify(minHeap)
        res = 0
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visited:
                continue
            visited.add(n1)
            res = w1

            for n2, w2 in adj[n1]:
                if n2 in visited:
                    continue
                heapq.heappush(minHeap, [w2 + w1, n2])
            
        return res if len(visited) == n else -1