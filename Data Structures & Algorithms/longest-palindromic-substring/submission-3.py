class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False] * len(s) for _ in range(len(s))]
        prev = ""
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if j-i<=2 and s[i] == s[j]:
                    dp[i][j] = True
                    string = s[i:j+1]
                    if len(string) > len(prev):
                        prev = string
                elif dp[i+1][j-1] == True and s[i] == s[j]:
                    dp[i][j] = True
                    string = s[i:j+1]
                    if len(string) > len(prev):
                        prev = string
                else:
                    dp[i][j]==False
        return prev
                