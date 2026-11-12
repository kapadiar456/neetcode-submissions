class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        res = []
        def dfs(val, count):
            if val>amount:
                return

            if val==amount:
                res.append(count)
                return

            if val in memo:
                return memo[val]

            for coin in coins:
                dfs(coin+val, count+1)
            return
        dfs(0, 0)

        if res == []:
            return -1
        else:
            return min(res)
                
            

