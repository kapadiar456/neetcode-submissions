class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0 for _ in range(len(nums)+1)]
        dp[-1] = max(nums)+1
        count = 0
        for i in range(len(nums)-1, -1, -1):
            if nums[i] < dp[i+1]:
                dp[i] = nums[i]
                count+=1
            else:
                dp[i] = dp[i+1]
        return count
