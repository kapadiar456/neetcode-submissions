class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0 for _ in range(len(cost)+1)]
        top = len(cost)
        dp[0] = cost[0]
        for i in range(len(cost)):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        for val in dp:
            print(val)
        return dp[-3]
        [1, 2, 3]
        [1, ]
            
