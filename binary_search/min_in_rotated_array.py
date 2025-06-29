#153. Find Minimum in Rotated Sorted Array (Medium)

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # No hints
        # Compiled to Debug

        if len(nums) == 1:
            return nums[0]
        
        left = 0
        right = len(nums) - 1

        if nums[left] < nums[right]:
            return nums[left]

        while left < right - 1:
            mid = (left + right) // 2
            if nums[left] < nums[mid]:
                left = mid
            else:
                right = mid
        
        return nums[right]