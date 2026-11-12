class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0 for _ in range(len(s)+1)]
        maxVal = 0
        endPos = len(s)-1
        for i in range(len(s)-1, -1, -1):
            if s[i] == '0':
                endPos = i
                continue
            val = int(s[i:endPos+1])
            if 1 <= val <= 26:
                dp[i] = dp[i+1] + 1
                endPos = i
        return dp[0]