class Solution:
    def rob(self, nums: List[int]) -> int:
        m1, m2 = 0, 0
        maxVal = 0
        for i in range(len(nums)):
            maxVal = max(m2, nums[i]+m1)
            m1 = m2
            m2 = maxVal

        return maxVal