class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        hashmap = {}
        nums.sort()
        cantUse = {}
        res = []
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]]=i
            else:
                hashmap[nums[i]]=i
        l = 0
        r = len(nums)-1
        for i in range(len(nums)):
            firstVal = nums[i]
            for j in range(len(nums)):
                if i==j:
                    continue
                secondVal = nums[j]
                total = secondVal+firstVal
                diff = 0 - total
                print("values: ",firstVal," ",secondVal," ",diff)
                if diff in hashmap:
                    if hashmap[diff]==i or hashmap[diff]==j or cantUse[i]>=1 or cantUse[j]>=1:
                        continue
                    cantUse[i] = 1 + cantUse.get(i, 0)
                    cantUse[j] = 1 + cantUse.get(j, 0)
                    res.append([secondVal,diff,firstVal])
            
            
            
        return res

