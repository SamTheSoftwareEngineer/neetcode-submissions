class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0 

        s = s.split()
        
        last_word = len(s[len(s) - 1])
        

        return last_word
        
        