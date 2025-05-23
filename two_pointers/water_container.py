#11. Container With Most Water (Medium)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # No hints
        left = 0
        right = len(height) - 1
        max_water = 0
        while left < right:
            cur_water = min(height[left], height[right]) * (right - left)
            if max_water < cur_water:
                max_water = cur_water
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        
        return max_water
        