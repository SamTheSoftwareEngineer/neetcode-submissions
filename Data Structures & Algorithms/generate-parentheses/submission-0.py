class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # res will store the overall result of our problem
        # Sol will be one of each of the valid solutions (a list of brackets that we will later join into a string)
        res, sol = [], []

        if n == 1:
            res.append('()')
            return res
        
        def backtrack(openn, close):
            if len(sol) == 2*n:
                res.append(''.join(sol))
                return 
            
            if openn < n:
                sol.append('(')
                backtrack(openn + 1, close)
                sol.pop()
            
            if openn > close:
                sol.append(')')
                backtrack(openn, close+1)
                sol.pop()

            
        backtrack(0,0)
        return res
        

        
