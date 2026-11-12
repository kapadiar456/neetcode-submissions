class Solution:
    def climbStairs(self, n: int) -> int:
        res = []
        def dfs(total):
            if total >n:
                return
            if total == n:
                res.append(1)
                return
            dfs(total+1)
            dfs(total+2)
            return res


        dfs(0)
        count=0
        for i in range(len(res)):
            count+=res[i]

        return count

