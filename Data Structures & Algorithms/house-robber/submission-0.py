class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1 = 0 # max money from houses up to i-2
        rob2 = 0 # max money from houses up to i-1

        for n in nums:
            new_rob = max(n + rob1, rob2)
            rob1, rob2 = rob2, new_rob
        return rob2


        
