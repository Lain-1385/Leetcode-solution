class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        def firstWord(s:str, word:str):
            if len(word) > len(s):
                return False 
            for i in range(len(word)):
                if not s[i] == word[i]:
                    return False
            return True
        dp = [False] * (len(s)+1)
        dp[0] = True
        k = 0

        while k < len(s):
            if dp[k] == True:
                for i in wordDict:
                    if firstWord(s[k:],i):
                        dp[k + len(i)] = True
            k += 1
        return dp[len(s)]
        
#better
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break

        return dp[-1]