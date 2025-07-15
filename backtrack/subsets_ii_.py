# 90. Subsets II (Medium)

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        cur, res = [], []

        def backtrack(i):
            if i >= len(nums):
                res.append(cur[:])
                return
            cur.append(nums[i])
            backtrack(i+1)
            cur.pop()

            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtrack(i+1)

        backtrack(0)
        return res
        
