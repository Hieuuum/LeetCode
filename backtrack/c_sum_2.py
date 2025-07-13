# 80. Combination Sum II (Medium)

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        res = []

        candidates = sorted(candidates)

        def backtrack(i, cur, total):
            if total == target and cur not in res:
                res.append(cur[:])
                return
            if i >= n or total > target:
                return
            
            cur.append(candidates[i])
            backtrack(i+1, cur, total + candidates[i])
            cur.pop()

            while i+1 < n and candidates[i] == candidates[i+1]:
                i += 1
            backtrack(i+1, cur, total)
            
        backtrack(0, [], 0)
        return res