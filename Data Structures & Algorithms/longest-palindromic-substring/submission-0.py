class Solution:
    def longestPalindrome(self, s: str) -> str:
        res, resLen = 0, 0
        palindrome = ''
        for i in range(len(s)):
            l = i
            if len(s)%2==0:
                r = i+1
            else:
                r = i
            while l>=0 and r<len(s):
                if s[l] == s[r]:
                    temp = s[l:r+1]
                    if r-l+1 > resLen:
                        palindrome = temp
                        resLen = r-l+1
                l-=1
                r+=1
        return palindrome