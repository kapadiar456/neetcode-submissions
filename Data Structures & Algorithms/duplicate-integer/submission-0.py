class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = {}
        for i in range(len(nums)):
            if nums[i] not in map:
                map[nums[i]]=1
            elif map[nums[i]] == 1:
                return True
            else:
                map[nums[i]]+=1
        return False