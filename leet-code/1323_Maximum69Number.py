class Solution:
    def maximum69Number (self, num):
        div = 1000
        while div > 0:
            temp = num // div
            if temp > 10:
                temp = temp % 10
            if temp == 6:
                num += (3 * div)
                break
            div //= 10
        return num
