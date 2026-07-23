class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        frequency_map = Counter(nums)
        unique = set()

        for key, value in frequency_map.items():
            if value == 1:
                unique.add(key)
            
        return max(unique) if unique else -1