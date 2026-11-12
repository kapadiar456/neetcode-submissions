class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        size = len(nums)-1
        for i in range(len(nums)-1):
            temp = max(nums[i] + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        rob3, rob4 = 0, 0
        for i in range(1, len(nums)):
            temp = max(nums[i] + rob3, rob4)
            rob3 = rob4
            rob4 = temp
        return max(rob4, rob2)