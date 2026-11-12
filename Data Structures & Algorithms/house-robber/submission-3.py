class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0 for _ in range(len(nums))]
        # [2, 9, 10, 11]
        for i in range(len(nums)):
            dp[i] = max(nums[i]+dp[i-2], dp[i-1]) 
        return dp[-1]
        