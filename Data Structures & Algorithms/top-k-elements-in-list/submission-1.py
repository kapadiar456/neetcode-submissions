class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        bucket = [[] for _ in range(len(nums)+1)]
        for i in range(len(nums)):
            hashmap[nums[i]] = hashmap.get(nums[i], 0) + 1
        
        for key, value in hashmap.items():
            bucket[value].append(key)
        ans = []
        for i in range(len(bucket)-1, -1, -1):
            print(bucket[i])
            if bucket[i] == None:
                continue
            else:
                for j in range(len(bucket[i])):
                    if k==0:
                        break
                    ans.append(bucket[i][j])
                    k-=1
        return ans
