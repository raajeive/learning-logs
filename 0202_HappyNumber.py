def findSquareDigits(num):
    res = 0
    while num != 0:
        temp = num % 10
        num = num // 10
        res += (temp * temp)
    return res


class Solution:
    def isHappy(self, n):
        resSet = set()
        while True:
            n = findSquareDigits(n)
            if n == 1:
                return True
            if n in resSet:
                return False
            resSet.add(n)
