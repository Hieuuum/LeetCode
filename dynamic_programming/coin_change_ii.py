# 518. Coin Change II (Medium)

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for i in range(1, amount + 1):
                dp[i] += dp[i - coin] if i >= coin else 0
        
        return dp[amount]