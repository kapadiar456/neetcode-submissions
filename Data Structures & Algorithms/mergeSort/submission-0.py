# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        def merge(arr, s, e):
            if (e-s)+1<=1:
                return arr
            m = (s+e)//2
            merge(arr, s, m)
            merge(arr, m+1, e)
            sort(arr, s, e , m)
            return arr
        def sort(arr, s, e, m):
            L = arr[s:m+1]
            R = arr[m+1: e+1]
            l = 0
            r = 0 
            k=s
            while l<len(L) and r<len(R):
                if L[l].key<=R[r].key:
                    arr[s]=L[l]
                    s+=1
                    l+=1
                else:
                    arr[s] = R[r]
                    s+=1
                    r+=1
            while l<len(L):
                    arr[s]=L[l]
                    s+=1
                    l+=1
            while r<len(R):
                    arr[s]=R[r]
                    s+=1
                    r+=1
        return merge(pairs, 0, len(pairs))

            
