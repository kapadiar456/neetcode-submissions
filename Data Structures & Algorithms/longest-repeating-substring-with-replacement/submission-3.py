class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if s == '':
            return 0
        l = 0
        r = 0
        mainChar = s[0]
        maxLength = 0
        count = k
        val =0
        while l < len(s)-1:
            if r == len(s):
                break
            if count == 0 and s[r] != mainChar:
                l = r
                count = k
            elif count != 0 and s[r] != mainChar:
                count-=1
            charLength = r-l+1
            maxLength = max(maxLength, charLength)
            r+=1
        return maxLength
            

