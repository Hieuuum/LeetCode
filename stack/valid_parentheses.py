# 20. Valid Parenthesis (Easy)

class Solution:
    def isValid(self, s: str) -> bool:
        
        bracket_dict = {'(': ')', '{': '}', '[': ']'}
        brackets = []

        for b in s:
            if b in "([{":
                brackets.append(b)
            else:
                if not brackets:
                    return False

                open_bracket = brackets.pop()

                if bracket_dict[open_bracket] != b:
                    return False
        
        if brackets:
            return False
            
        return True