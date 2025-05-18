#LeetCode 217. Contains Duplicate
class Solution:
    def containsDuplicate(self, nums) -> bool: #nums: List[int]
        return len(set(nums)) != len(nums)