class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = dict()
        
        for i in range(len(nums)):

             # Check if the complement (the difference) exists in the 'hash' dictionary
            if not (target - nums[i] in hash):
                # If it doesn't exist, store the current number as a key and its index as a value
                hash[nums[i]] = i
            else:
                # If the complement exists in the 'hash', it means we found a pair
                # Return the indices of the two numbers that add up to the target
                return [hash[target - nums[i]], i]
        return []