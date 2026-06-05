class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        res = ""

        for s in strs:
            res += str(len(s))  + "#" + s
        
        return res

    def decode(self, s: str) -> List[str]:
        pointer = 0
        res = []
        
        while pointer < len(s):
            j = pointer
            while s[j] != "#":
                j += 1
            
            length = int(s[pointer:j])

            pointer = j + 1

            word = s[pointer:pointer + length]
            res.append(word)

            pointer = pointer + length
    
        return res

        

                

