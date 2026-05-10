class Solution:
    def isPalindrome(self, s: str) -> bool:
        modified_string = ''

        s = s.lower()

        for char in s:
            if char.isalnum():
                modified_string += char 
        
        return modified_string == modified_string[::-1]