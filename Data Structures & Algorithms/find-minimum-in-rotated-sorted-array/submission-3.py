class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 25, 1, 2, 3, 4
        l = 0
        r = len(nums)-1
        minVal = 0
        lowest = 0
        k = 0
        while l<=r:
            mid = l+ (r-l) // 2
            if nums[mid]<nums[r]:
                r = mid
            else:
                l = mid + 1

        return nums[mid]