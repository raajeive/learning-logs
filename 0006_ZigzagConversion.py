class Solution:
    def convert(self, s, numRows):
        if numRows == 0:
            return None
        elif numRows == 1:
            return s
        else:
            result = [""] * numRows
            index = 0
            step = 1
            for x in s:
                result[index] += x
                if index == 0:
                    step = 1
                elif index == numRows - 1:
                    step = -1
                else:
                    pass
                index += step
            return "".join(result)
