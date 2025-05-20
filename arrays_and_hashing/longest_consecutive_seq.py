#128. Longest Consecutive Sequence (Medium)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Many hints
        nums_set = set(nums)
        max_len = 0
        for num in nums_set:
            if num-1 not in nums_set:
                cur = num
                count = 1
                while cur+1 in nums_set:
                    count += 1
                    cur += 1
                max_len = max(max_len, count)

        return max_len