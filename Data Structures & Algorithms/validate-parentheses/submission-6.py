class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {']':'[', ')':'(', '}':'{'}
        stack = []
        for brac in s:
            if brac in hashmap and hashmap[brac] == stack[-1]:
                stack.pop()
            else:
                stack.append(brac)
        if len(stack)==0:
            return True
        else:
            return False

