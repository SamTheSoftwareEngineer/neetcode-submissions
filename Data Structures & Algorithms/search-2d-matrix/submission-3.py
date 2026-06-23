class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Flatten the matrix first, then apply binary search (does not meet time complexity requirements)
        # combined_array = []

        # for row in range(len(matrix)):
        #     for col in range(len(matrix[row])):
        #         combined_array.append(matrix[row][col])

        # print(combined_array)

        # l = 0
        # r = len(combined_array) - 1

        # while l <= r:
        #     mid = l + ((r - l) // 2)
        #     if combined_array[mid] > target:
        #         r = mid - 1
        #     elif combined_array[mid] < target:
        #         l = mid + 1
        #     else:
        #         return True
        
        # return False
        rows, cols = len(matrix), len(matrix[0])
        
        top = 0
        bottom = rows - 1

        while top <= bottom:
            row = (top + bottom) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row - 1
            else: break

        
        if not (top <= bottom):
            return False
        
        row = (top + bottom) // 2
        l, r = 0, cols - 1
        while l <= r:
            m = (l+r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else: 
                return True
        
        return False
        

