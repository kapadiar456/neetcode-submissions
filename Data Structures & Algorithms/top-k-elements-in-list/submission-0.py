class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]]=1
            else:
                hashmap[nums[i]]+=1
        List = [[] for _ in range(len(nums)+1)]
        for number, occurances in hashmap.items():
            List[occurances].append(number)
        finalList = []
        for i in range(len(List)-1, 0, -1):
            for num in List[i]:
                finalList.append(num)
                if len(finalList) == k:
                    return finalList
        return finalList
