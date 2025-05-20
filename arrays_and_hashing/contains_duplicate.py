#217. Contains Duplicate (Easy)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # No hints
        return len(set(nums)) != len(nums)