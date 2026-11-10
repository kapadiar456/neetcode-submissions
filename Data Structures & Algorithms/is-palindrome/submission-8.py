class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s)==1:
            return True
        l = 0 
        r = len(s)-1
        while l < r:
            print(s[l]," " ,s[r])
            while s[l].isalnum() == False and l<r:
                l+=1
            while s[r].isalnum() == False and r>l:
                r-=1
            print(s[l]," " ,s[r])
            if s[l].lower() != s[r].lower():
                return False
            else:
                l+=1
                r-=1
        return True