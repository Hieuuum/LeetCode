#594. Longest Harmonious Subsequence

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        
        count = collections.Counter(nums)
        if len(count) == 1:
            return 0
        
        max_len = 0
        for num, num_count in count.items():
            if num-1 in nums:
                max_len = max(num_count + count[num-1], max_len)
        
        return max_len