class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, vals, total):
            if total == target:
                res.append(vals.copy())
                return
            for j in range(i, len(nums)):
                if total + nums[j]>target:
                    return
                vals.append(nums[j])
                dfs(j, vals, total+nums[j])
                vals.pop()
        dfs(0,[],0)
        return res