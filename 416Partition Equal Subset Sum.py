from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums.sort()
        total = sum(nums)
        if not total % 2 == 0:
            return False
        target = total // 2
        dp = [[False, set()] for _ in range(total)]
        dp[0][0] = True
        length = len(nums)
        for i in range(0,target):
            if dp[i][0] == True:
                cur_max = max(dp[i][1]) if dp[i][1] else 0
                for j in range(cur_max, length):
                        if not j in dp[i][1]:
                            dp[i + nums[j]][0] = True
                            dp[i + nums[j]][1] = dp[i][1].copy()
                            dp[i + nums[j]][1].add(j)
        return dp[target][0]

x = Solution()
a = [1,2,5]
x.canPartition(a)

#better
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]

        return dp[target]