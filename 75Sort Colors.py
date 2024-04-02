class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums) - 1
        i = 0
        while i < right + 1:
            if nums[i] == 2:
                temp1 = nums[right]
                nums[right] = 2
                nums[i] = temp1
                right -= 1
                i -= 1
            elif nums[i] == 0:
                temp2 = nums[left]
                nums[left] = 0
                nums[i] = temp2
                left += 1
            i += 1
        return nums
    
#better
class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        low, mid, high = 0, 0, len(nums) - 1
        
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
    