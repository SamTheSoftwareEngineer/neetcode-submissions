class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_values = set()
         
        for number in nums:
            if number in unique_values:
                return True
            else:
                unique_values.add(number)
        return False 