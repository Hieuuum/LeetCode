# 424. Longest Repeating Character Replacement (Medium)

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Hint 3
        # Compile to Debug
        
        left = 0
        max_len = 0
        max_char = 0
        char_count = {}

        for right in range(len(s)):
            cur_char = s[right]
            char_count[cur_char] = char_count.get(cur_char, 0) + 1
            
            max_char = max(max_char, char_count[cur_char])
            if right - left + 1 - max_char <= k:
                max_len = max(max_len, right - left + 1)
            while right - left + 1 - max_char > k:
                char_count[s[left]] -= 1
                left += 1

        return max_len