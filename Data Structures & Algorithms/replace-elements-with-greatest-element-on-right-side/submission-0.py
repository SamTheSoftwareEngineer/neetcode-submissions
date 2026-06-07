class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        right_max = -1

        # reverse iteration
        for i in range(n - 1, -1, -1):
            # new max = max(oldmax, arr[i])
            newMax = max(right_max, arr[i])
            arr[i] = right_max
            right_max = newMax
        
        return arr
            
