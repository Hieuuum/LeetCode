# 78. Subsets (Medium)

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, sol = [], []

        def backtracking(i):
            if i == n:
                # Append to res
                res.append(sol[:])
                return
            
            # Don't pick nums[i]
            backtracking(i+1)

            # Pick nums[i]
            sol.append(nums[i])
            backtracking(i+1)
            sol.pop()
        
        backtracking(0)
        return res