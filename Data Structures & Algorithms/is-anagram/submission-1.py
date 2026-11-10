class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1 = {}
        map2 = {}
        for i in range(len(s)):
            if s[i] not in map1:
                map1[s[i]]=1
            else:
                map1[s[i]]+=1
        for i in range(len(t)):
            if t[i] not in map2:
                map2[t[i]]=1
            else:
                map2[t[i]]+=1
        if map1==map2:
            return True
        else:
             return False
        