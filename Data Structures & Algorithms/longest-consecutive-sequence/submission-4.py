class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)
        # 3, 2, 1
        for val in nums:
            hashmap[val] +=1
        maxLength = 1
        for i in range(len(nums)):
            curr = nums[i]
            count = 1
            while curr+1 in hashmap:
                maxLength = max(maxLength, count)
                curr = curr+1
                count+=1
        return maxLength+1