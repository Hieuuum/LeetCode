# 739. Daily Temperatures (Medium)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # No hints
        # Compile to Debug
        
        days = len(temperatures)
        result = [0] * days
        stack = []

        for i in range(days-1, -1, -1):
            while stack and stack[-1][0] <= temperatures[i]:
                stack.pop()
            
            if stack:
                result[i] = stack[-1][1] - i

            stack.append((temperatures[i], i))
            
        return result
