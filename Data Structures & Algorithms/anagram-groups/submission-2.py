class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mainHashmap = defaultdict(list)
        res = [[] for i in range(len(strs))]
        i= 0
        for x in range(len(strs)):
            word = strs[x]
            charArray = [0] * 26
            for char in word:
                charArray[ord(char)-ord('a')]+=1
            mainHashmap[tuple(charArray)].append(word)
        return list(mainHashmap.values())
