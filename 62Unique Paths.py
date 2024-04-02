class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n] *m

        for i in range(m):
            dp[i][0] = 1
        for i in range(n):
            dp[0][i] = 1

        for R in range(1, m) :
            for C in range(1, n):
                path_up = dp[R - 1][C] if R > 0 else 0
                path_left = dp[R][C - 1] if C > 0 else 0
                dp[R][C] = path_left + path_up
        return dp[m - 1][n - 1]