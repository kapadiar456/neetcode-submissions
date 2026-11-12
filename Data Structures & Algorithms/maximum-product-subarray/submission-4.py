class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dpMin = [1 for _ in range(len(nums)+1)]
        dpMax = [1 for _ in range(len(nums)+1)]
        minVal = 1
        maxVal = 1
        prevMax = 0
        for i in range(len(nums)):
            maxVal = max(nums[i]*maxVal, nums[i]*minVal, nums[i])
            minVal = min(nums[i]*maxVal, nums[i]*minVal, nums[i])
            dpMin[i] = minVal
            dpMax[i] = maxVal
            prevMax = max(maxVal, prevMax)
        return prevMax
