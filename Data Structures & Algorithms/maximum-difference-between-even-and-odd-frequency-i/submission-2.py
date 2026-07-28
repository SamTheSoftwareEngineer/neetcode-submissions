class Solution:
    def maxDifference(self, s: str) -> int:
        frequency_map = Counter(s)
        diff1 = 0
        diff2 = float('inf')

        print(frequency_map)

        for key in frequency_map.keys():
            if frequency_map[key] % 2 != 0:
                diff1 = max(diff1, frequency_map[key])
                print(diff1)
            else:
                diff2 = min(diff2, frequency_map[key])
                print(diff2)

        return diff1 - diff2