class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr1 = [0 for _ in range(len(nums)+1)]
        hashmap = defaultdict(int)
        for val in nums:
            hashmap[val]+=1
        for key, val in hashmap.items():
            arr1[val] = key
        res = []
        for i in range(len(arr1)-1,-1,-1):
            print(arr1[i], "k ", k)
            if k==0:
                break
            if arr1[i]==0:
                continue
            else:
                res.append(arr1[i])
                k-=1
        return res