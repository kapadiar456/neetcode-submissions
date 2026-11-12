class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        minVal = nums[0]
        while l < r:
            mid = (r+l)//2
            if nums[mid] > nums[r]:
                minVal = nums[r]
                l = mid+1
            else:
                if nums[mid]<nums[l]:
                    minVal = nums[mid]
                    l = mid
                else:
                    minVal = nums[l]
                    r=mid
        return minVal
