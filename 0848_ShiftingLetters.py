class Solution:
    def shiftingLetters(self, s, shifts):
        total = sum(shifts)
        s = list(s)
        for i in range(len(s)):
            s[i] = chr(((ord(s[i]) - ord("a")) + total) % 26 + ord("a"))
            total -= shifts[i]
        return "".join(s)
