class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dis = 0
        final = len(nums)-1
        i = 0
        while i < len(nums)-1:
            if nums[i] == 0:
                return False
            dis += nums[i]
            i = dis
            print(i)
        if i == final:
            return True
        else:
            return False