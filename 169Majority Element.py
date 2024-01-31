class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        length = len(nums)
        dict = {}
        for i in nums:
            if i in dict:
                dict[i] += 1
                if dict[i] > length / 2:
                    return i
            else:
                dict[i] = 0
        return i
    
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0
        for i in nums:
            if count == 0:
                candidate = i
            if i == candidate:
                count += 1
            else:
                count -= 1
        return candidate