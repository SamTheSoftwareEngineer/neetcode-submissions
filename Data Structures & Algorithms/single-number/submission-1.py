class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_count = {}

        for num in nums:
            num_count[num] = num_count.get(num, 0) + 1
        
        for key, value in num_count.items():
            if value == 1:
                return key
