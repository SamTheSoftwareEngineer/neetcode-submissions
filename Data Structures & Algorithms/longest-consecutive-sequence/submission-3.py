class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        res = 0

        curr, longest = nums[0], 0
        i = 0

        while i < len(nums):
            if curr != nums[i]:
                curr = nums[i]
                longest = 0
            while i < len(nums) and nums[i] == curr:
                i += 1
            longest += 1
            curr += 1
            res = max(res, longest)
        return res

        
        