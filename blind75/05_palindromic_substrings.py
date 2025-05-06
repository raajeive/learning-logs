class Solution:
    def countSubstrings(self, s: str) -> int:

        def countPalindrom(left, right):
            temp_count = 0
            while left >=0 and right < len(s) and s[left] == s[right]:
                temp_count = temp_count + 1
                left = left - 1
                right = right + 1
            return temp_count


        count = 0
        for idx in range(len(s)):
            count = count + countPalindrom(idx, idx) + countPalindrom(idx, idx + 1)
        return count
