class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        length = 1
        longest_so_far = 1
        nums.sort()

        for i in range(len(nums) - 1):
            if nums[i+1] - nums[i] == 1:
                length += 1
            elif nums[i+1] - nums[i] == 0:
                continue
            else:
                length = 1
            
            if length > longest_so_far:
                longest_so_far = length
        
        return longest_so_far