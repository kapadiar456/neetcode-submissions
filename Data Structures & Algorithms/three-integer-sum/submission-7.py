class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        hashmap = {}
        #nums.sort()
        cantUse = {}
        res = []
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]]=i
            else:
                hashmap[nums[i]]=i
        l = 0
        r = len(nums)-1
        print(nums)
        for i in range(len(nums)):
            firstVal = nums[i]
            for j in range(len(nums)):
                if i==j:
                    continue
                secondVal = nums[j]
                total = secondVal+firstVal
                diff = 0 - total
                if diff in hashmap:
                    if hashmap[diff]==i or hashmap[diff]==j:
                        continue
                    numList = [secondVal,diff,firstVal]
                    numList.sort()
                    print(numList)
                    if numList in res:
                        continue
                    else:
                        res.append(numList)
            
            
            
        return res

