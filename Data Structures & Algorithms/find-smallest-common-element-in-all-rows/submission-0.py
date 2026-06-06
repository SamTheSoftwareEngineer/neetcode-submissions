class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        frequency_count = {}
        total_rows = 0

        for row in mat:
            total_rows += 1
            for element in row:
                frequency_count[element] = frequency_count.get(element, 0) + 1

        for key, count in frequency_count.items():
            if count == total_rows:
                return key
        
        return -1
            
            
