class Solution:
    def longestCommonPrefix(self, strs):
        res_len = 0
        breakit = False
        for i in range(len(strs[0])):
            for word in strs:
                if not (i < len(word) and strs[0][:i + 1] == word[:i + 1]):
                    res_len = i
                    breakit = True
                    break
            else:
                res_len += 1        
            if breakit:
                break
        return strs[0][:res_len]
