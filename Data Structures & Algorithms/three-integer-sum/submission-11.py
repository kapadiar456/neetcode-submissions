class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)-1):
            l = i+1
            r = len(nums)-1
            while l < r:
                trip = nums[l]+nums[r]+nums[i]
                if trip < 0:
                    l+=1
                elif trip > 0:
                    r-=1
                else:
                    if [nums[i], nums[l], nums[r]] not in res: 
                        res.append([nums[i], nums[l], nums[r]])
                    l+=1
                
        return res