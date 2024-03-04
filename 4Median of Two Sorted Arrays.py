'''
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len_sum = len(nums1) + len(nums2)

        isodd = True if len_sum % 2 == 1 else False

        len_a = len(nums1)
        len_b = len(nums2)
        left_a, right_a = 0, len(nums1)

        while True:
            mid_a = (left_a + right_a) // 2
            # 
            if mid_a == len_a:
                return nums2[(len_sum - 1) // 2 - len_a] if isodd else \
                    (nums2[(len_sum - 1) // 2 - len_a] + nums2[(len_sum - 1) // 2 - len_a + 1]) / 2.0
            if mid_a == 0:
                return nums1[(len_sum - 1) // 2 - len_b] if isodd else \
                    (nums1[(len_sum - 1) // 2 - len_b] + nums1[(len_sum - 1) // 2 - len_b + 1]) / 2.0
            # the count num of left of total is (len_sum -1 //2) , index: 0 to len_sum - 1 //2 - 1
            check_index = len_sum // 2 - mid_a -1 
            if check_index < 0 or check_index > len_b - 1:
                    break
            # the left of total sum should contain[0: mid_a +1] ,[0:check_index] 
            if nums1[mid_a] <= nums2[check_index]:
                if nums1[mid_a + 1] >= nums2[check_index]:
                    return min(nums2[check_index], nums1[mid_a + 1]) if isodd else \
                        (nums2[check_index] + nums1[mid_a + 1]) / 2.0

                else:
                    left_a = mid_a + 1
            else:
                # left 0 , mid_a - 1; 0 , check_index
                if nums1[mid_a - 1] <= nums2[check_index]:
                    return max(nums2[check_index], nums1[mid_a])
                else:
                    #TODO : check right_a = mid_a -1 or mid_a
                    right_a = mid_a - 1
'''
# better
# 我们要找到的是这样一个i，使得A[i-1]<=B[j]且B[j-1]<=A[i]
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 确保nums1是较短的数组
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        total_length = len(nums1) + len(nums2)
        half = total_length // 2
        
        left, right = 0, len(nums1) - 1
        while True:
            mid1 = (left + right) // 2
            mid2 = half - mid1 - 2
            
            nums1LeftMax = nums1[mid1] if mid1 >= 0 else float("-infinity")
            nums1RightMin = nums1[mid1 + 1] if (mid1 + 1) < len(nums1) else float("infinity")
            
            nums2LeftMax = nums2[mid2] if mid2 >= 0 else float("-infinity")
            nums2RightMin = nums2[mid2 + 1] if (mid2 + 1) < len(nums2) else float("infinity")
            
            # 找到正确的分割
            if nums1LeftMax <= nums2RightMin and nums2LeftMax <= nums1RightMin:
                # 如果总长度是奇数
                if total_length % 2:
                    return min(nums1RightMin, nums2RightMin)
                # 如果总长度是偶数
                return (max(nums1LeftMax, nums2LeftMax) + min(nums1RightMin, nums2RightMin)) / 2
            elif nums1LeftMax > nums2RightMin:
                right = mid1 - 1
            else:
                left = mid1 + 1
