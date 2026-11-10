class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        hashmap = defaultdict(int)
        # 3, 2, 1
        for val in nums:
            hashmap[val] +=1
        maxLength = 1
        for i in range(len(nums)):
            curr = nums[i]
            count = 1
            while curr+1 in hashmap:
                curr = curr+1
                count+=1
                maxLength = max(maxLength, count)
        return maxLength