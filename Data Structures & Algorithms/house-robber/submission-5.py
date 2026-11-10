class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp = [0 for _ in range(len(nums))]
        # if len(nums)==1:
        #     return nums[0]
        # if len(nums)==2:
        #     return max(nums[0], nums[1])
        # # [2, 9, 10, 11]
        # for i in range(len(nums)):
        #     dp[i] = max(nums[i]+dp[i-2], dp[i-1]) 
        # return dp[-1]
        m1, m2 = 0, 0
        maxVal = 0
        for i in range(len(nums)):
            maxVal = max(m1, nums[i]+m2)
            m2 = m1
            m1 = maxVal
        return maxVal
            

        