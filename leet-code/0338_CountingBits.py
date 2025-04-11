class Solution:
    def countBits(self, n):
        res = [0]
        for num in range(1, n + 1):
            res.append(res[num >> 1] + num % 2)
        return res
