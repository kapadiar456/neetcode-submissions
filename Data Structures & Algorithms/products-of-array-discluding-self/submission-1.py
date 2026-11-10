class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1,2,4,6]
        res = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            res[i] = nums[i-1]*res[i-1]
        # [1,1,2,8]
        res2 = [1 for _ in range(len(nums))]
        for i in range(len(nums)-2, -1, -1):
            res2[i]= res2[i+1]*nums[i+1]
        for i in range(len(nums)):
            res[i]=res[i]*res2[i]
        return res

