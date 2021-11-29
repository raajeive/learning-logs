/*
Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

https://leetcode.com/problems/longest-substring-without-repeating-characters
*/

int lengthOfLongestSubstring(char * s){
    int left = 0;
    int right = 0;
    int hash[128] = {0};
    int res = 0;
    while(s[right] != '\0'){
        hash[(int)s[right]] += 1;
        while(hash[(int)s[right]] > 1){
            hash[(int)s[left]] -= 1;
            left += 1;
        }
        if(res < right - left + 1){
            res = right - left + 1;
        }
        right += 1;
    }
    return res;
}
