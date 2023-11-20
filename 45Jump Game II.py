class Solution:
    def jump(self, nums: List[int]) -> int:
        # dp[i] = dp[j] + 1 (0<= j <= i j is the first element which can jump to i)
        n = len(nums)
        if n == 1:
            return 0;

        dp = [0] * n
        dp[0] = 0
        dp[1] = 1
        j = 0

        for i in range(2,n):
            # find the first j to jump i
            while j + nums[j] < i:
                j += 1
            dp[i] = dp[j] + 1

        return dp[n - 1]