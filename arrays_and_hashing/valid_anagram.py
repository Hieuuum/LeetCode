#242. Valid Anagram (Easy)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = {}
        for letter in s:
            if letter not in s_list:
                s_list[letter] = 1
            else:
                s_list[letter] += 1

        t_list = {}
        for letter in t:
            if letter not in t_list:
                t_list[letter] = 1
            else:
                t_list[letter] += 1
        
        for letter in s:
            if letter not in t or t_list[letter] != s_list[letter]:
                return False

        for letter in t:
            if letter not in s or t_list[letter] != s_list[letter]:
                return False
        
        return True