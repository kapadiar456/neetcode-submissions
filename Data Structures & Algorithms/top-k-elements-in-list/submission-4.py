class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr1 = [[] for _ in range(len(nums)+1)]
        hashmap = defaultdict(int)
        for val in nums:
            hashmap[val]+=1
        for key, val in hashmap.items():
            arr1[val].append(key)
        res = []
        for i in range(len(arr1)-1,-1,-1):
            if k==0:
                break
            for num in arr1[i]:
                res.append(num)
                k-=1
                if k == 0: break
        return res