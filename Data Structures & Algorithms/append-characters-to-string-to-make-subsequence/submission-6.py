class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        t_pointer = 0
        s_pointer = 0
        longest_prefix_length = 0

        while s_pointer < len(s) and t_pointer < len(t):
            if s[s_pointer] == t[t_pointer]:
                longest_prefix_length += 1
                t_pointer += 1
            
            s_pointer += 1 
        

        return len(t) - longest_prefix_length
