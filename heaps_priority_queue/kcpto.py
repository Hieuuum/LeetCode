#973. K Closest Points to Origin (Medium)

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)

        for point in points:
            x, y = point[0], point[1]
            dist = -math.sqrt(point[0]**2 + point[1]**2)
            heapq.heappush(heap, (dist, [x, y]))
        
        while len(heap) > k:
            heapq.heappop(heap)
        
        res = []
        while heap:
            cur = heapq.heappop(heap)
            res.append(cur[1])

        return res
