class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        minVal = 1
        maxVal = 1
        prevMax = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                maxVal = 1
                minVal = 1
                continue
            temp = maxVal * nums[i]
            maxVal = max(nums[i]*maxVal, nums[i]*minVal, nums[i])
            minVal = min(temp, nums[i]*minVal, nums[i])
            prevMax = max(maxVal, prevMax)
        return prevMax
