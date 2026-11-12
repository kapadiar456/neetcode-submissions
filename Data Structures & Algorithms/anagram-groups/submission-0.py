class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def compare(string1, string2):
            hashmap1 = {}
            hashmap2 = {}
            for char in string1:
                if char not in hashmap1:
                    hashmap1[char]=1
                else:
                    hashmap1[char]+=1
            for char in string2:
                if char not in hashmap2:
                    hashmap2[char]=1
                else:
                    hashmap2[char]+=1
            if hashmap1 == hashmap2:
                return True
            else:
                return False
        masterlist = []
        used = []
        for string in strs:
            tempList = []
            if string not in used:
                tempList.append(string)
            for word in strs:
                if not string == word and compare(string, word)==True and word not in used:
                    used.append(word)
                    used.append(string)
                    tempList.append(word)
            if not tempList == []:
                masterlist.append(tempList)
        return masterlist

        