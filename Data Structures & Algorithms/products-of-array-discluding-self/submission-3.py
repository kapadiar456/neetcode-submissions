class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1, 1, 2, 8
        # 48, 24, 6, 1
        arr1 = [1 for _ in range(len(nums))]
        arr2 = [1 for _ in range(len(nums))]

        for i in range(1, len(nums)):
            arr1[i] = nums[i-1] * arr1[i-1]
            
        for i in range(len(nums)-2, -1, -1):
            arr2[i] = nums[i+1] * arr2[i+1]
        
        res = []
        for i in range(len(nums)):
            print('1 ', arr1[i] ,'2', arr2[len(nums)-i-1])
            res.append(arr1[i] * arr2[i])
        
        return res