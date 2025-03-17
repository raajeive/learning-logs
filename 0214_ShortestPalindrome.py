"""
You are given a string s. You can convert s to a palindrome by adding characters in front of it.

Return the shortest palindrome you can find by performing this transformation.

Input: s = "aacecaaa"
Output: "aaacecaaa"

https://leetcode.com/problems/shortest-palindrome/
"""

# Approach 1, find the largest palindrom from begining
# and reverse and add the remaining in the front
class Solution:
    def check_pal(self, s):
        s_rev = s[::]
        s_rev.reverse()
        if s == s_rev:
            return True
        return False

    def shortestPalindrome(self, s):
        str_list = [i for i in s]
        max_index_pal = 0
        i = 1
        while(i < len(str_list)):
            if self.check_pal(str_list[:i+1]):
                max_index_pal = i
            i += 1
        new_str_list = str_list[max_index_pal+1:]
        new_str_list.reverse()
        new_str = "".join(new_str_list) + "".join(str_list)
        return new_str
