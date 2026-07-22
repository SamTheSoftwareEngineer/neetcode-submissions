class Solution:
    def confusingNumber(self, n: int) -> bool:
        rotation_map = {
            '0' : '0',
            '1' : '1',
            '2' : False,
            '3' : False,
            '4' : False,
            '5' : False,
            '6' : '9',
            '7' : False,
            '8' : '8',
            '9' : '6'
        }

        
        num = str(n)[::-1]
        reversed_n = ""

        for digit in num:
            if rotation_map[digit] != False:
                reversed_n += rotation_map[digit] 

            else:
                return False
        
        if int(reversed_n) != n:
            return True
        
        return False
        

            