class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Used hints
        left_i = 0
        right_i = len(s)-1

        while left_i <= right_i:
            while left_i <= right_i and not s[left_i].isalnum():
                left_i += 1
            while left_i <= right_i and not s[right_i].isalnum():
                right_i -= 1

            if left_i <= right_i:
                left_char = s[left_i].lower()
                right_char = s[right_i].lower()
                if left_char != right_char:
                    return False
            left_i += 1
            right_i -= 1

        return True