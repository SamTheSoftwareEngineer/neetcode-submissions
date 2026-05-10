class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        number_count = {}
        for number in nums:
            number_count[number] = number_count.get(number, 0) + 1 
        
        for key, value in number_count.items():
            if value == 1:
                return key