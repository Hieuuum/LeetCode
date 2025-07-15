# 17. Letter Combinations of a Phone Number (Medium)

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        cur, res = [], []

        digitToChars = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(i):
            if i >= len(digits):
                res.append("".join(cur))
                return
            for char in digitToChars[digits[i]]:
                cur.append(char)
                backtrack(i+1)
                cur.pop()
        
        if digits:
            backtrack(0)
        return res
