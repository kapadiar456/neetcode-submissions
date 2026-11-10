class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [1 for _ in range(len(s)+1)]
        maxVal = 0
        endPos = len(s)-1
        for i in range(len(s)-1, -1, -1):
            print(s[i:endPos+1])
            if s[i] == '0':
                dp[i]=0
                continue
            else:
                dp[i] = dp[i+1]
            if i + 1 < len(s) and 1 <= int(s[i:i+2]) <= 26:
                dp[i] += dp[i+2]
        return dp[0]