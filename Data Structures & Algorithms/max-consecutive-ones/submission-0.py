class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # Set a variable to keep track of the consecutive ones
        max_ones = 0
        consecutive_ones = 0
        # Loop through the array and check each element if its a 1 or 0
        # Increment our consective_ones variable
        # Update our max_ones variable with the max we've seen so far 
        
        for i in range(len(nums)):
            if nums[i] == 1:
                consecutive_ones += 1
                if consecutive_ones > max_ones:
                    max_ones = consecutive_ones
            else:
                consecutive_ones = 0

        return max_ones