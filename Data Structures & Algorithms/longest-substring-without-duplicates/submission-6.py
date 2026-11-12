class Solution:
    def meetsdef (self, myList):
        myMap = {}
        for i in range(len(myList)):
            myMap[myList[i]] = 1 + myMap.get(myList[i],0)
        for k,v in myMap.items():
            if v ==2:
                return True
        return False

    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==1:
            return 1
        maxLength = 0
        l = 0
        r = 0
        while r<len(s):
            window = s[l:r]
            print("window ",s[l:r] )
            while self.meetsdef(s[l:r])==True:
                l+=1
            maxLength = max(maxLength, len(s[l:r]))
            r+=1
        return maxLength
