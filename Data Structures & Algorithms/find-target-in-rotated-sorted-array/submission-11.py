class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(l: int, r: int, target: int):
            while l<=r:
                mid = (r+l)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    r = mid-1
                else:
                    l = mid + 1
            return -1

        l = 0
        r = len(nums) - 1
        mid = -1
        while l <= r:
            mid = (r+l)//2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]:
                ans = binarySearch(l, mid, target)
                if ans == -1:
                    l = mid+1
                else:
                    return ans
            else:
                ans = binarySearch(mid, r, target)
                if ans == -1:
                    r = mid-1
                else:
                    return ans
        return -1
