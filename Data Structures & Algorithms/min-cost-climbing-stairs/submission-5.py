class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0 for _ in range(len(cost)+1)]
        top = len(cost)
        for i in range(2, len(cost)+1):
            dp[i] = min(cost[i-1] + dp[i-1], cost[i-2] + dp[i-2])
        
        return dp[top]
            
