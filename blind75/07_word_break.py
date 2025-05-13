class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        dp = [True] + [False] * len(s)

        for idx in range(1, len(s) + 1):
            for word in wordDict:
                start = idx - len(word)
                if start >= 0 and dp[start] and s[start:idx] == word:
                    dp[idx] = True

        return dp[-1]
