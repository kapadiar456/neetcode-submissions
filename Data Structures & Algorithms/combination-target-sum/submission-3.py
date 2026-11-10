class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(index, total, curr):
            if total == target:
                res.append(curr.copy())
                return
            for i in range(index, len(nums)):
                if total + nums[i] > target:
                    continue
                curr.append(nums[i])
                total+=nums[i]
                dfs(i, total, curr)
                curr.pop()
                total-=nums[i]
            return
        dfs(0, 0, [])
        return res