#3. Longest Substring Without Repeating Characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Hint 3
        # Compiled to Debug

        left = 0
        max_length = 0
        char_set = set()
        
        for right in range(len(s)):
            cur_char = s[right]
            if cur_char not in char_set:
                char_set.add(s[right])
            else:
                max_length = max(max_length, len(char_set))
                while s[left] != cur_char:
                    char_set.remove(s[left])
                    left += 1
                left += 1
        
        max_length = max(max_length, len(char_set))
        return max_length
