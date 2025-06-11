#567. Permutation in String (Medium)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Hint 3
        # Compiled to Debug
        
        # Edge case where s1 is longer than s2
        if len(s1) > len(s2):
            return False
        
        # Initialize dictionaries for character frequency
        s1_freq = {}
        window_freq = {}
        
        # Populate the frequency dictionary for s1
        for char in s1:
            s1_freq[char] = s1_freq.get(char, 0) + 1
        
        # Sliding window of size len(s1) over s2
        for i in range(len(s2)):
            # Add the current character to the window's frequency dictionary
            window_freq[s2[i]] = window_freq.get(s2[i], 0) + 1
            
            # Once the window size exceeds len(s1), remove the left-most character
            if i >= len(s1):
                left_char = s2[i - len(s1)]
                if window_freq[left_char] == 1:
                    del window_freq[left_char]
                else:
                    window_freq[left_char] -= 1
            
            # Check if the window matches s1's frequency
            if window_freq == s1_freq:
                return True
        
        return False