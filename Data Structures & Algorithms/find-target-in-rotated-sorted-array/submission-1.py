class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (r+l)//2
            currVal = nums[mid]
            if currVal == target:
                return mid
            elif currVal < nums[r] and currVal < target:
                l = mid + 1
            else:
                if currVal < nums[l] and currVal < target:
                    r = mid -1
                elif currVal >=nums[l] and currVal > target:
                    l = mid
                else:
                    return -1
        return currVal
