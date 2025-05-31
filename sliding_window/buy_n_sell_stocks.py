#121. Best Time to Buy and Sell Stock (Easy)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # No hints
        if len(prices) < 2:
            return 0

        max_price = prices[-1]
        profit = 0
        for i in range(len(prices)-2, -1, -1):
            if max_price < prices[i]:
                max_price = prices[i] 
            elif profit < max_price - prices[i]:
                profit = max_price - prices[i]
        
        return profit
        