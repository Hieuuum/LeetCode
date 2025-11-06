# 494. Target Sum (Medium)

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1 # 1 way to sum up to 0 with 0 elements

        for i in range(len(nums)):
            next_dp = defaultdict(int)
            for val, count in dp.items():
                next_dp[val + nums[i]] += dp[val]
                next_dp[val - nums[i]] += dp[val]
            dp = next_dp
        
        return dp[target]