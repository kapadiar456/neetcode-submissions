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
            print('l: ',l, 'r: ',r)
            print(mid)
            if nums[mid] < nums[l] and nums[mid] < nums[r]:
                r = mid
                lowest = mid
            else:
                l +=1
                

        return nums[mid]