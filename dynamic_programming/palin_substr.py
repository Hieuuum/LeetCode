# 647. Palindromic Substring (Medium)

class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        for i in range(len(s)):
            l = i
            r = i
            while 0 <= l and r <= len(s)-1 and s[l] == s[r]:
                l -= 1
                r += 1
                count += 1
            
            l = i
            r = i+1
            while 0 <= l and r <= len(s)-1 and s[l] == s[r]:
                l -= 1
                r += 1
                count += 1
        
        return count
            