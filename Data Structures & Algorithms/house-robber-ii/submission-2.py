class Solution:
    def rob(self, nums: List[int]) -> int:
        m1, m2 = 0, 0
        maxVal = 0
        for i in range(len(nums)-1):
            maxVal = max(m1, nums[i]+m2)
            m2 = m1
            m1 = maxVal

        m3, m4 = 0, 0
        maxVal2 = 0
        for i in range(1, len(nums)):
            maxVal2 = max(m3, nums[i]+m4)
            m4 = m3
            m3 = maxVal2
        print(maxVal2)
        return max(maxVal, maxVal2)
        