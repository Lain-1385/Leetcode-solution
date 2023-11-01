class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        
        result = set()
        for i in range(len(nums)):

            # delete repeated i
            if(i > 0 and nums[i] == nums[i-1]):
                continue

            hash = {}
            for j in range(i+1,len(nums)):
                if not - nums[i] - nums[j] in hash:
                    hash[nums[j]]= 1
                else:
                    result.add(tuple(sort_3(nums[i], - nums[i] - nums[j], nums[j])))
        return result
    
def sort_3(a, b, c):
    if a > b:
        a, b = b, a
    if a > c:
        a, c = c, a
    if b > c:
        b, c = c, b
    return a, b, c
        