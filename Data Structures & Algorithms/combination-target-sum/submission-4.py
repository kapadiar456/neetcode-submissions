class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        def dfs(i, res, total):
            if total > target:
                return
            if total == target:
                ans.append(list(res))
                return
            if i >=len(nums):
                return
            val = nums[i]

            res.append(val)
            dfs(i, res, total + val)
            res.pop()
            dfs(i+1, res, total)
            return
        dfs(0, [], 0)
        return ans

