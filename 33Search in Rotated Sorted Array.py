class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        mid = (left + right) // 2
        # pivot 0 , 0 ,mid ,last
        # pivot is in the first half, order: mid ,last, 0
        # pivot second half, order: last, 0, mid
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                if target > nums[right] and nums[left] > nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if target < nums[left] and nums[mid] > nums[right]:
                    left = mid + 1
                else:
                    right = mid -1
        return -1 

# better 
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # Check if left half is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # Otherwise, right half is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1