class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        for i in range(len(nums)):
            if i > max_reach:
                return False
            max_reach = max(nums[i] + i, max_reach)

            if max_reach >= len(nums)-1:
                return True
        return False