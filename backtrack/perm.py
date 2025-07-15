# 46. Permutations (Medium)

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        numList = set()
        cur, res = [], []
        def backtrack():
            if len(cur) == len(nums):
                res.append(cur[:])
                return
            for i in range(len(nums)):
                if nums[i] not in numList:
                    cur.append(nums[i])
                    numList.add(nums[i])
                    backtrack()
                    cur.pop()
                    numList.remove(nums[i])
        
        backtrack()
        return res