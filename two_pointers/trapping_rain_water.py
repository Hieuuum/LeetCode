#42. Trapping Rain Water
class Solution:
    def trap(self, height: List[int]) -> int:
        # Used hints
        
        left = 0
        right = len(height) - 1
        max_left = 0
        max_right = 0
        total_water = 0
        
        while left < right:
            if height[left] > height[right]:
                if max_right >= height[right]:
                    total_water += max_right - height[right]
                else:
                    max_right = height[right]
                right -= 1
            else:
                if max_left >= height[left]:
                    total_water += max_left - height[left]
                else:
                    max_left = height[left]
                left += 1

        return total_water
                
            








