class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if s == '':
            return 0
        l = 0
        r = 0
        mainChar = s[0]
        maxLength = 0
        count = k
        while l < len(s)-1:
            if count==0:
                l = r
                count = k
            elif s[r] != mainChar:
                count-=1
            charLength = r-l+1
            maxLength = max(maxLength, charLength)
            r+=1
            if r == len(s)-1:
                break
        return maxLength+1
            

