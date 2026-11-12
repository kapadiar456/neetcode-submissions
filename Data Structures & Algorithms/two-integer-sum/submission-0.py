class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums)-1
        while (i<j):
            print(str(nums[i])+ " " + str(nums[j]))
            total = nums[i] + nums[j]
            if total==target:
                return [i, j]
            elif total > target:
                j-=1
            else:
                i+=1
            