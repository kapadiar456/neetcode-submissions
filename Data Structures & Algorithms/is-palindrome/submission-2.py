class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = len(s) - 1 
        l = 0
        while (l<r):
            while not s[l].isalnum():
                l+=1
            while not s[r].isalnum() and r>l:
                r-=1
            rightChar = s[r].lower()
            leftChar = s[l].lower()
            print(leftChar +  ' ' + rightChar)
            if rightChar!=leftChar:
                return False
            l+=1
            r-=1
        return True