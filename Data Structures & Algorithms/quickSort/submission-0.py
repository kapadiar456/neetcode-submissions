# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        def sort(arr, s, e):
            if (e-s)+1<=1:
                return arr
            pivot = arr[e]
            left = s
            for i in range(s,e):
                if arr[i].key<pivot.key:
                    temp = arr[i]
                    arr[i]=arr[left]
                    arr[left]=temp
                    left+=1
            arr[e] = arr[left]
            arr[left] = pivot
            sort(arr,s, left-1)
            sort(arr,left+1,e)
            return arr
        return sort(pairs,0,len(pairs)-1)

        