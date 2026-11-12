class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        minVal = float('-inf')
        for val in nums:
            if val >= minVal:
                minVal = val
        arr1 = [0 for _ in range(minVal+1)]

        for i in range(len(nums)):
            arr1[nums[i]]+=1
        res = []
        for i in range(len(arr1)-1, -1, -1):
            if k==0:
                break
            if arr1[i] > 0:
                k-=1
                res.append(i)
        return res

        