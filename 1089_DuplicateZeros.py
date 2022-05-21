class Solution:
    def duplicateZeros(self, arr):
        """
        Do not return anything, modify arr in-place instead.
        """
        zeroes = arr.count(0)
        length = len(arr)
        for index in range(length - 1, -1, -1):
            if index + zeroes < length:
                arr[index + zeroes] = arr[index]
            if arr[index] == 0:
                zeroes -= 1
                if index + zeroes < length:
                    arr[index + zeroes] = 0

