class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        
        stack = [] # pair: [temp, index]

        # We enumerate the temperatures array to get an index:temp pair 
        for index, temp in enumerate(temperatures):
            # While our stack is non-empty and if the current temp we are on is greater
            # than the one on the top of our stack
            while stack and temp > stack[-1][0]:
                # We can pop the value off the top of our stack and store its 
                # temp and index 
                stackT, stackInd = stack.pop()
                # We calculate the diff between the index we are currently on and 
                # the index of the temp we just popped 
                res[stackInd] = (index - stackInd)
            
            # If the stack is empty or we see a temp that is less than the one on top of the stack,
            # wwe append the temp:index pair to our stack 
            stack.append([temp,index])
        return res 
            
        
