# 309. Best Time to Buy and Sell Stock with Cooldown (Medium)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {} #(i, canBuy) = max_val

        def dfs(i, canBuy):
            if i >= len(prices):
                return 0
            
            cooldown = dfs(i+1, canBuy)
            if canBuy:
                buy = dfs(i+1, not canBuy) - prices[i]
                dp[(i, canBuy)] = max(buy, cooldown)
            else:
                sell = dfs(i+2, not canBuy) + prices[i]
                dp[(i, canBuy)] = max(sell, cooldown)
            
            return dp[(i, canBuy)]
            
        return dfs(0, True)