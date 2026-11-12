class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        if len(s)==2:
            if s[0]==s[1]:
                return 1
            else:
                return 2
        if len(s)==0:
            return 0
        l = 0
        r = 1
        maxLength = 1
        while r<len(s):
            window = s[l:r]
            print("window: ", window)
            maxLength = max(maxLength, len(window))
            while s[r] in window:
                l+=1
                window = s[l:r]
            r+=1
        return maxLength

            