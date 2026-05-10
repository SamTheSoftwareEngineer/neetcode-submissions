class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = {}
        arr = []
        res = []

        for number in nums:
            frequency_map[number] = frequency_map.get(number, 0) + 1
        
        for element, frequency in frequency_map.items():
        # Append each frequency and its element to the ans array
           arr.append([frequency, element])
        arr.sort()
        print(arr)

        res = []
        while k > 0:
            res.append(arr.pop()[1])
            k -= 1 
        return res 

         