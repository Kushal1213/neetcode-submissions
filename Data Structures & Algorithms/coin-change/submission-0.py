class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp  = [0] * (amount+1)
        dp[0] = 0 

        coins.sort()

        for i in range(1,amount+1):
            minn = float('inf')
            for c in coins:
                rem = i - c
                if rem < 0:
                    break 
                minn = min(minn,dp[rem]+1)
            dp[i] = minn
        return dp[amount] if dp[amount]!= float('inf') else  -1
