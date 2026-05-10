class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_of_chars_s = {}
        count_of_chars_t = {}

        for char in s:
            count_of_chars_s[char] = count_of_chars_s.get(char, 0) + 1
        
        for char in t:
            count_of_chars_t[char] = count_of_chars_t.get(char, 0) + 1
        
        return count_of_chars_s == count_of_chars_t
        
        
