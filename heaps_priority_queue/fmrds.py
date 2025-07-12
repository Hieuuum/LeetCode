# 295. Find Median From Data Stream (Hard)

class MedianFinder:

    def __init__(self):
        self.count = 0
        self.minHeap, self.maxHeap = [], []

    def addNum(self, num: int) -> None: # 2, 3
        heapq.heappush(self.minHeap, num)
        self.count += 1

        while len(self.minHeap) - len(self.maxHeap) > 1:
            cur = -heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, cur)
        
        while self.minHeap and self.maxHeap and self.minHeap[0] < -self.maxHeap[0]:
            num1, num2 = heapq.heappop(self.minHeap), -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, num2)
            heapq.heappush(self.maxHeap, -num1)
        
    def findMedian(self) -> float:
        if self.count % 2 == 1:
            return self.minHeap[0]
        else:
            return (self.minHeap[0] - self.maxHeap[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()