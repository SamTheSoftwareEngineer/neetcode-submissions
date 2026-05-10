class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = {}
        temp_array = []
        res = []

        for number in nums:
            # Count the number of times each value occurs
            frequency_map[number] = frequency_map.get(number, 0) + 1
        
        # Access the key & frequency by accessing the map's items
        for key, frequency in frequency_map.items():
            temp_array.append([frequency, key])
        temp_array.sort()
        
        while k > 0:
            res.append(temp_array.pop()[1])
            print(res)
            k -= 1
        return res 

        

        
        
            
            