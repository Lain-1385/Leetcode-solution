class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        new_set = set()
        for i in nums:
            if i in new_set:
                return True
            else:
                new_set.add(i)
        return False
    

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num = set(nums)
        if len(num)<len(nums):
            return True
        return False