"""
Given a string s, return the longest palindromic substring in s.

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.

https://leetcode.com/problems/longest-palindromic-substring/
"""

# solution 1 O(n^3)
class Solution(object):
    def longestPalindrome(self, s):
        def is_palindrome(l, r):
            while l < r :
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        longest = (0, 0)
        for left in range(len(s)):
            for right in range(left, len(s)):
                if is_palindrome(left, right):
                    longest = max(longest, (left, right), key=lambda x:x[1] - x[0])
        return s[longest[0]:longest[1] + 1]

 
# solution 2 O(n^2)
class Solution(object):
    def longestPalindrome(self, s):
        def palindrome(l, r):
            if s[l] != s[r]:
                return 0, 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return l + 1, r - 1

        longest = (0, 0)
        for idx in range(len(s) - 1):
            longest = max(longest, max(palindrome(idx, idx), palindrome(idx, idx + 1), key=lambda x:x[1] - x[0]), key=lambda x:x[1] - x[0])
        return s[longest[0]:longest[1] + 1]
