class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute force
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # return []

        # Optimized solution
        # Create an empty hashmap to hold the indices and number pairs
        num_index = {}

        for index, number in enumerate(nums):
            diff = target - number
            if diff in num_index:
                return [num_index[diff], index]
            else:
                num_index[number] = index 
                
        
