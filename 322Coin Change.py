class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #TODO: analyse the note
        #coins.sort(reverse=True)
        if amount == 0:
            return 0

        if min(coins) > amount:
            return -1
        
        memo = {}
        def recursion(amount):
            if amount in memo:
                return memo[amount]

            if amount < 0:
                return -1
            if amount == 0:
                return 0
            
            min_sub = amount + 1
            for j in coins:
                #if min_sub < amount / j: 
                #    break
                temp = recursion(amount - j)
                if temp > -1:
                    min_sub = min(min_sub, temp)

            if min_sub == amount + 1:
                memo[amount] = -1 
                return -1
            
            memo[amount] = min_sub + 1
            return min_sub + 1
        return recursion(amount)
        '''
        # dp[n] = min(dp[n-i])+ 1
        if amount == 0:
            return 0

        min_coins = min(coins)
        if min_coins > amount:
            return -1
        elif min_coins == amount:
            return 1

    

        dp = [-1] * (amount + 1)
        dp[0] = 0


        for i in range(min_coins,amount + 1):
            min_dp = amount + 1
            for j in coins:
                if i < j:
                    continue
                if dp[i - j] >= 0:
                    min_dp = min(min_dp,dp[i - j])
            if min_dp == amount + 1:
                dp[i] = -1
            else:
                dp[i] = min_dp + 1
        return dp[amount]
        '''