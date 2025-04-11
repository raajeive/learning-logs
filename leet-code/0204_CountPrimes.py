from math import ceil, sqrt
class Solution:
    def countPrimes(self, n):
        if n <= 2:
            return 0
        prime = [True] * n
        prime[0] = prime[1] = False

        sqrtn = ceil(sqrt(n))
        for i in range(2, sqrtn):
            if prime[i]:
                for j in range(i * i, n, i):
                    prime[j] = False
        return sum(prime)
