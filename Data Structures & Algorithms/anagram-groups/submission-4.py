class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Loop through each string and create a map of it
        hashmap = defaultdict(list)
        for word in strs:
            arr = [0 for _ in range(26)]
            for character in word:
                arr[ord('z')-ord(character)] += 1
            hashmap[tuple(arr)].append(word)
        res = []
        for k, v in hashmap.items():
            res.append(v)
        return res
            