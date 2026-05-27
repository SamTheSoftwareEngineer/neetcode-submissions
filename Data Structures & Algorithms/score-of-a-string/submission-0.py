class Solution:
    def scoreOfString(self, s: str) -> int:

        current_score = 0 

        for i in range(len(s) - 1):
            score = abs(ord(s[i]) - ord(s[i+1]))
            current_score += score

        return current_score
            
