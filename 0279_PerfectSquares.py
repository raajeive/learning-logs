import sys
from math import sqrt
class Solution:
    def numSquares(self, n):
        if n <= 0:
            return 0
        dp = [sys.maxsize] * (n + 1)
        dp[0] = 0
        
        for i in range(1, n + 1):
            
            end = int(sqrt(i)) + 1
            for j in range(1, end):
                dp[i]  = min(dp[i], dp[i - j * j] + 1)
        return dp[-1]
        

