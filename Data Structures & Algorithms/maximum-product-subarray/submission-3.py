class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dpMin = [0 for _ in range(len(nums))]
        dpMax = [0 for _ in range(len(nums))]
        res = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            if i==0:
                dpMin[i]=nums[i]
                dpMax[i]=nums[i]
                res[i] = nums[i]
                continue
            else:
                dpMin[i]= min(nums[i], dpMin[i-1]*nums[i], dpMax[i-1]*nums[i])
                dpMax[i]= max(nums[i], dpMin[i-1]*nums[i], dpMax[i-1]*nums[i])
                res[i] = max(dpMax[i], res[i-1])
        return res[-1]

