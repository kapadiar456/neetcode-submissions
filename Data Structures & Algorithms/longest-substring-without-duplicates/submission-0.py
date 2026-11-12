class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
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
                #maxLength = max(maxLength, len(window))
            r+=1
        return maxLength

            