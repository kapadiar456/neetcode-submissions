class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s)==1:
            return False
        hashmap = {'}':'{',']':'[',')':'('}
        for bracket in s:
            if bracket in hashmap:
                if len(stack)>0 and  stack[-1] == hashmap[bracket]:
                    stack.pop()
                    continue
            stack.append(bracket)
        print (stack)
        return len(stack)==0

            