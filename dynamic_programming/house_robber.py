# 198. House Robber (Medium)

class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for num in nums:
            temp = max(rob2 + num, rob1)
            rob2, rob1 = rob1, temp
        
        return rob1