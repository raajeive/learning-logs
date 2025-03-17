class Solution:
    def nthUglyNumber(self, n):
        ugly = [1]
        i2, i3, i5 = 0, 0, 0
        while n > 1:
            u2, u3, u5 = ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5
            umin = min(u2, u3, u5)
            ugly.append(umin)
            if umin == u2:
                i2 += 1
            if umin == u3:
                i3 += 1
            if umin == u5:
                i5 += 1
            else:
                pass
            n -= 1
        return ugly[-1]
