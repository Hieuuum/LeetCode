# 131. Palindrome Partitioning (Medium)

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        cur, res = [], []
        
        def isPalindrome(s):
            i, j = 0, len(s)-1
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        def backtrack(i):
            if i >= len(s):
                res.append(cur[:])
            for j in range(i, len(s)):
                if isPalindrome(s[i:j+1]):
                    cur.append(s[i:j+1])
                    backtrack(j+1)
                    cur.pop()
        
        backtrack(0)
        return res

        

