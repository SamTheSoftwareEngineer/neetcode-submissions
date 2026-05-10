class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        frequency_count = {}

        for number in nums:
            frequency_count[number] = frequency_count.get(number, 0) + 1
        
        for key, value in frequency_count.items():
            if value > 1:
                return True
        
        return False 