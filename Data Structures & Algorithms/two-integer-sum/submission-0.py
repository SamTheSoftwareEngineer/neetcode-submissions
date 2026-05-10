class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        index_value = {}

        for index, value in enumerate(nums):
            diff = target - value
            if diff in index_value:
                return [index_value[diff], index]
            else:
                index_value[value] = index 