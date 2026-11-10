class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        hashmap = defaultdict(int)
        res = []
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j == i:
                    continue
                twoSum = nums[j]+nums[i]
                val = 0-twoSum
                if val in hashmap and hashmap[val] != i and hashmap[val] != j:
                    newList = [nums[j], nums[i], val]
                    newList.sort()
                    if newList not in res:
                        res.append(newList)
        return res