class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1 for _ in range(len(nums))]
        for i in range(len(nums)):
            if i>0:
                ans[i] = nums[i-1] * ans[i-1]
        for val in ans:
            print(val)
        ans2 = [1 for _ in range(len(nums))]
        for i in range(len(nums)-1,-1,-1):
            if i<len(nums)-1:
                ans2[i] = ans2[i+1] * nums[i+1]
        finalAns = []
        for i in range(len(nums)):
            finalAns.append(ans[i]*ans2[i])
        return finalAns
        