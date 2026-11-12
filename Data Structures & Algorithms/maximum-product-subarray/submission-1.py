class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = [1 for _ in range(len(nums)+1)]
        # [2,3,-2,4]
        # [1,2,1,1,1]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i-1]*nums[i])
        return dp[len(nums)-1]
