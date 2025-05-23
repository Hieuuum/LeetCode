#1. Two Sum
class Solution(object):
    def twoSum(self, nums, target):
        #No hints
        diff = {}
        for i, num in enumerate(nums):
            cur_diff = target - num
            if cur_diff not in diff:
                diff[num] = i
            else:
                return [diff[cur_diff], i]