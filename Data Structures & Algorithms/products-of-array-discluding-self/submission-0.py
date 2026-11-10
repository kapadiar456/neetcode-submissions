class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_array = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            product=1
            for j in range(len(nums)):
                if j==i:
                    continue
                product*=nums[j]
            product_array[i]=product
        return product_array