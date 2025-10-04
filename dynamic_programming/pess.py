# 416. Partition Equal Subset Sum (Medium)

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        else:
            target = sum(nums) // 2
        
        dp = [False] * (target+1)
        dp[0] = True

        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]

        return dp[target]