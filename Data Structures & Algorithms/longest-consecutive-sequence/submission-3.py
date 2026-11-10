class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = hashmap.get(nums[i], 0) + 1
        ans = 1
        for k, v in hashmap.items():
            curr = k
            length = 1
            while curr+1 in hashmap:
                length+=1
                curr+=1
            ans = max(ans,length)
        return ans


            

