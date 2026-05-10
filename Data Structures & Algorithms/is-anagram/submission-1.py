class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_of_s = Counter(s)
        count_of_t = Counter (t)

        return count_of_s == count_of_t

        
        
