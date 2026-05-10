class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums
        else:
            l, r = 0, k
            
            max_window = []
            
            while l < r and r < len(nums) + 1:
                max_window.append(max(nums[l:r]))
                l += 1
                r += 1 
                
            return max_window
        
            