# 787. Cheapest Flights Within K Stops (Medium)

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0      
        for _ in range(k+1):
            tmpPrices = prices.copy()
            for s, d, c in flights:
                tmpPrices[d] = min(tmpPrices[d], prices[s] + c)
            print(tmpPrices)
            prices = tmpPrices
        
        
        return prices[dst] if prices[dst] != float('inf') else -1

