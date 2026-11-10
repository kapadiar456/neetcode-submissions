class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = {}
        for number in nums:
            if number not in hashmap:
                hashmap[number]=1
            else:
                hashmap[number]+=1
        numList = []
        for k, v in hashmap.items():
            numList.append(k)
        longest = 0
        lists = []
        seq =[]
        for num in numList:
            if num-1 not in numList:
                length =1
                while num+length in numList:
                    length+=1
                longest = max(longest,length)

        return longest

            

