class Solution:
    def climbStairs(self, n: int) -> int:
        # c[n] = c[n-1] + c[n-2]
        if n == 1:
            return 1
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2,n + 1):
            dp[i] = dp[i - 1] +dp[i - 2]
        return dp[n]