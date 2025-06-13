# 76. Minimum Window Substring (Hard)

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Hint 3
        # Compiled to Debug

        if s == "" or t == "" or len(s) < len(t):
            return ""
        
        window, t_count = {}, {}

        for c in t:
            t_count[c] = t_count.get(c, 0) + 1

        have, need = 0, len(t_count)
        res, resLen = [-1, -1], float('inf')
        l = 0
        for r in range(len(s)):
            r_char = s[r]

            if r_char not in t_count:
                continue

            window[r_char] = window.get(r_char, 0) + 1
            
            if window[r_char] == t_count[r_char]:
                have += 1

            while have == need:
                if resLen > r - l + 1:
                    res = [l, r]
                    resLen = r - l + 1

                l_char = s[l]

                if l_char not in t_count:
                    l += 1
                    continue

                window[l_char] -= 1
                if window[l_char] < t_count[l_char]:
                    have -= 1
                
                l += 1

        if resLen != float("inf"):
            l, r = res
            return s[l:r+1]
        else:
            return ""


