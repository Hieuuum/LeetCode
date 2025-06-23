# 22. Generate Parentheses (Medium)

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # No hints
        # No IDE debug
        
        stack = []
        res = []

        stack.append(("", 0, 0))

        while stack:
            cur = stack.pop()
            if len(cur[0]) == 2*n:
                res.append(cur[0])
            
            if cur[1] - cur[2] > 0:
                if cur[1] < n:
                    stack.append((cur[0] + "(", cur[1] + 1, cur[2]))
                
                if cur[2] < n:
                    stack.append((cur[0] + ")", cur[1], cur[2] + 1))
            
            else:
                stack.append((cur[0] + "(", cur[1] + 1, cur[2]))

        return res
