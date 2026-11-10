class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap1 = {}
        hashmap2 = {}
        for i in range(0, len(s)):
            if s[i] in hashmap1:
                hashmap1[s[i]] += 1
            else:
                hashmap1[s[i]] = 1
        for j in range (0, len(t)):
            if t[j] in hashmap2:
                hashmap2[t[j]] += 1
            else:
                hashmap2[t[j]] = 1
        if hashmap1 == hashmap2:
            return True
        else:
            return False