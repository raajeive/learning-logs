class Solution:
    def maxHeight(self, cuboids):
        A = [[0, 0, 0]] + sorted(map(sorted, cuboids))
        N = len(A)
        dp = [0] * N
        for i in range(1, N):
            for j in range(i):
                if all([A[j][k] <= A[i][k] for k in range(3)]):
                    dp[i] = max(dp[i], dp[j] + A[i][2])
        return max(dp)
