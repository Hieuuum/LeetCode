# 1046. Last Stone Weight (Easy)

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            stoneA = -heapq.heappop(stones)
            stoneB = -heapq.heappop(stones)
            if stoneA > stoneB:
                heapq.heappush(stones, stoneB-stoneA)
        
        stones.append(0)
        return abs(stones[0])
