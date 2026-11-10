class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1 for _ in range(amount+1)]
        dp[0] = 0
        for i in range(1, len(dp)):
            for coin in coins:
                if i - coin>=0:
                    dp[i] = min(dp[i], 1 + dp[i-coin])
        if dp[-1] == amount+1:
            return -1
        return dp[-1]
        # I want to loop through and then add the prev answer
        # Each item in the array represents the min number of coins to reach that value
        # that can sum to your amount
        # coins = [1, 4, 5, 10]
        # example [0, 1, 2, 3, 1, 1]