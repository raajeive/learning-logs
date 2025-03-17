class Solution:
    def isPowerOfFour(self, n):
        return n and not (n & (n - 1)) and not((n - 1) % 3)

class Solution:
    def isPowerOfFour(self, n):
        while n != 0:
            if n == 1:
                return True
            elif n % 4 == 0:
                n = n / 4
            else:
                return False
