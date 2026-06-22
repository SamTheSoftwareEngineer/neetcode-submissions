class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        combined_array = []

        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                combined_array.append(matrix[row][col])

        print(combined_array)

        l = 0
        r = len(combined_array) - 1

        while l <= r:
            mid = l + ((r - l) // 2)
            if combined_array[mid] > target:
                r = mid - 1
            elif combined_array[mid] < target:
                l = mid + 1
            else:
                return True
        
        return False