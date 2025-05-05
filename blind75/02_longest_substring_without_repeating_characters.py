class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letter_set = set()
        start = 0
        max_length = 0
        for index in range(0, len(s)):
            while start <= index:
                if s[index] in letter_set:
                    letter_set.remove(s[start])
                    start = start + 1
                else:
                    break
            letter_set.add(s[index])
            max_length = max(max_length, index - start + 1)
        return max_length