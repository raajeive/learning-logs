class Solution:
    def lengthOfLongestSubstring(self, s):
        start = 0
        end = 0
        res = 0
        hashTable = {} 
        while(end < len(s)):
            if s[end] in hashTable:
                hashTable[s[end]] += 1
            else:
                hashTable[s[end]] = 1
            while hashTable[s[end]] > 1:
                hashTable[s[start]] -= 1
                start += 1
            res = max(res, end - start + 1)
            end += 1
        return res
