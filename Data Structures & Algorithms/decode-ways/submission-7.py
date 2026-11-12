class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0 for _ in range(len(s))]
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == '0':
                    continue
                val = int(s[i:j+1])
                if 1 <= val <= 26:
                    dp[i] = dp[j] + 1
                else:
                    continue
        return dp[0]