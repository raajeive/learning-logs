class Solution:
    def letterCombinations(self, digits):
        infoDict = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        res = []
        if len(digits) == 0:
            return []
        for item in infoDict[digits[0]]:
            res.append(item)
        for index in range(1, len(digits)):
            l = len(res)
            res = res * len(infoDict[digits[index]])
            a = 0
            for item in infoDict[digits[index]]:
                for i in range(a, a + l):
                    res[i] += item
                a += l
        return res
