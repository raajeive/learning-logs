import sys

class Solution:
    def coinChange(self, coins, amount):
        dp = [0] + [sys.maxsize] * amount
        for index in range(1, amount + 1):
            for coin in coins:
                if 0 <= index - coin <= amount:
                    dp[index] = min(dp[index], dp[index - coin] + 1)
        return [dp[-1], -1][dp[-1] == sys.maxsize]
