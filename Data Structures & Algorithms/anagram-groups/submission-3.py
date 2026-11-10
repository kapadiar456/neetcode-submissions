class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myMap = defaultdict(list)
        for word in strs:
            wordArray = [0 for _ in range(26)]
            for char in word:
                wordArray[ord('a')-ord(char)] += 1
            myMap[tuple(wordArray)].append(word)
        i=0
        final =[]
        for key, value in myMap.items():
            res = []
            for item in value:
                res.append(item)
            final.append(res)
        return final
                
            
            

