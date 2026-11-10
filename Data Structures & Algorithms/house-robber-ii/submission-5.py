class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        m1, m2 = 0, 0
        maxVal = 0
        for i in range(len(nums)-1):
            maxVal = max(m2, nums[i]+m1)
            m1 = m2
            m2 = maxVal

        m3, m4 = 0, 0
        maxVal2 = 0
        for i in range(1, len(nums)):
            maxVal2 = max(m4, nums[i]+m3)
            m3 = m4
            m4 = maxVal2

        return max(maxVal, maxVal2)
        