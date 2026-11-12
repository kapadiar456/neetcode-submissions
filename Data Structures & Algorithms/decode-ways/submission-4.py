class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s)==1 and int(s) == 0:
            return 0
        dp = [0 for _ in range(len(s)+1)]
        i = 0
        j = 0
        dp[0] = 1
        for j in range(1, len(s)):
            val = int(s[i:j])
            if 0 < val <=26:
                dp[j] += 1 + dp[j-1]
                j += 1
            elif val == 0:
                return 0
            else:
                while (not int(s[i:j])):
                    i+=1
        for val in dp:
            print(val)
        return dp[len(s)-1]