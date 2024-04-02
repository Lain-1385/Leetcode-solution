'''
#failed
class Solution:
    def longestPalindrome(self, s: str) -> str:
        #use dp to record the longest parlindrome from the end of s[i]
        dp = [1]* len(s)
        flag_allsame = [False]*len(s)
        for i in range(1, len(s)):
            if (flag_allsame[i-1] == True or dp[i - 1] == 1) and s[i] == s [i-1]:
                flag_allsame[i] = True
                dp[i] = dp[i - 1] + 1
            elif i - dp[i-1] > 0 and s[i] == s[i - dp[i-1] -1]:
                dp[i] = dp[i-1] + 2
            else:
                s_rever = s[-dp[i-1] + 1:][::-1]
                for i in 
        right = dp.index(max(dp))
        left = right - dp[right]
        return s[left+1:right+1]
'''
#dp
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        # Initialize the DP table
        dp = [[False] * n for _ in range(n)]
        start, max_length = 0, 1

        # Every single character is a palindrome
        for i in range(n):
            dp[i][i] = True

        # Check for palindromes of length 2
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                start = i
                max_length = 2

        # Check for palindromes of length 3 and more
        for length in range(3, n+1):
            for i in range(n-length+1):
                j = i + length - 1  # Ending index of the current substring
                # Checking the condition for DP
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    start = i
                    max_length = length
        
        # Return the longest palindrome substring
        return s[start:start+max_length]


#expand around center 
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) < 1:
            return ""
        
        start, end = 0, 0
        
        for i in range(len(s)):
            len1 = self.expandAroundCenter(s, i, i) # Odd length palindrome
            len2 = self.expandAroundCenter(s, i, i+1) # Even length palindrome
            len_max = max(len1, len2)
            if len_max > end - start:
                start = i - (len_max - 1) // 2
                end = i + len_max // 2
        
        return s[start:end + 1]
    
    def expandAroundCenter(self, s, left, right):
        L, R = left, right
        while L >= 0 and R < len(s) and s[L] == s[R]:
            L -= 1
            R += 1
        return R - L - 1
