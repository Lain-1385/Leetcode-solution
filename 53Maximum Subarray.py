class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = -9999999
        current_sum = 0
        for i in nums:
            current_sum += i
            res = max(current_sum, res)
            if current_sum < 0:
                current_sum = 0
        return res
    
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = len(nums) * [0]
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1],0) + nums[i]
        return max(dp)