# 84. Largest Rectangle In Histogram (Hard)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Hints
        # Compiled to Debug
        
        stack = [] # pair: (index, height)
        max_area = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                start = index
            stack.append((start, h))
        
        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))

        return max_area