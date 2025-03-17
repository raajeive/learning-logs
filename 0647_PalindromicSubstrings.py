"""
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

https://leetcode.com/problems/palindromic-substrings/
"""

# O(n^3)
class Solution:
    def countSubstrings(self, s: str) -> str:

        def subpalindromes(s):
            i, j = 0, len(s) - 1
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return 1
                
        total = 0
        for left in range(len(s)):
            for right in range(left, len(s)):
                total += subpalindromes(s[left:right + 1])
        return total


# fastest solution
class Solution:
    def countSubstrings(self, s: str) -> str:

        def subpalindromes(i, j):
            res = 0
            if j >= len(s) or s[i] != s[j]:
                return res
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
                res += 1
            return res
                
        total = 0
        for i in range(len(s)):
            total += subpalindromes(i, i)
            total += subpalindromes(i, i + 1)
        return total
