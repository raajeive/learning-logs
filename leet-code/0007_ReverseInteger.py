class Solution:
    def reverse(self, x: int) -> int:
        negativeFlag = False
        if x < 0:
            negativeFlag = True
        numStr = str(x) if not negativeFlag else str(x)[1:]
        num = int(numStr[::-1])
        if num < ((-1) * (2**31)) or num > ((2**31) - 1):
            return 0
        return num if not negativeFlag else ((-1) * num)
