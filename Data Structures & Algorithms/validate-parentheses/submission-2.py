class Solution:
    def isValid(self, s: str) -> bool:
        mapOfBrackets = {'}':'{',')':'(',']':'['}
        stack = []
        for brac in s:
            if brac in mapOfBrackets and not stack is None:
                stack.pop()
            stack.append(brac)
        if stack==None:
            return False
        else:
            return True
