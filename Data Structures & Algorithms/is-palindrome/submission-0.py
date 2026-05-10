class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        modified_string = ''

        for char in s:
            if char.isalnum():
                modified_string += char
        
        l, r = 0, len(modified_string) - 1

        while l < r:
            if modified_string[l] == modified_string[r]:
                l += 1
                r -= 1
            else:
                return False
        
        return True 