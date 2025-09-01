# 5. Longest Palindromic Substring (Medium)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0
        for i in range(len(s)):
            l = i
            r = i
            while r < len(s)-1 and s[l] == s[r+1]:
                r += 1

            while 0 < l and r < len(s)-1 and s[l-1] == s[r+1]:
                l -= 1
                r += 1
            
            if resLen < r - l + 1:
                resLen = r - l + 1
                res = s[l:r+1]
        
        return res
        