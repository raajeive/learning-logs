class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) <= 1:
            return s
        
        start = end = 0

        def expand_from_centre(left, right):

            nonlocal start, end

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left = left - 1
                right = right + 1
            
            if right - left - 1 > end - start:
                start = left + 1
                end = right - 1
        
        for idx in range(len(s)):
            expand_from_centre(idx, idx)
            expand_from_centre(idx, idx + 1)
        
        return s[start: end + 1]
