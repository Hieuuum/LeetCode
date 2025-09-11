# 300. Longest Increasing Subsequence (Medium)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        count = [1] * (len(nums))
        for i in range(len(nums)-2, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    count[i] = max(count[i], count[j] + 1)
                j += 1
        
        return max(count)
            