class MinHeap:
    
    def __init__(self):
        self.arr = [0]
        self.index = 1

    def push(self, val: int) -> None:
        #self.arr[self.index] = val
        self.arr.append(val)
        i=self.index
        while i>1 and self.arr[i] < self.arr[i//2]:
            temp = self.arr[i]
            self.arr[i] = self.arr[i//2]
            self.arr[i//2] = temp
            i=i//2
        self.index+=1

    def pop(self) -> int:
        if len(self.arr) == 1:
            return -1
        if len(self.arr) == 2:
            self.index-=1
            return self.arr.pop()
        ans=self.arr[1]
        print(self.arr[1])
        self.arr[1] = self.arr.pop()
        index=1
        self.bubbleDown(index)
        self.index-=1
        return ans

    def top(self) -> int:
        if self.index == 1:
            return -1
        else:
            return self.arr[1]

    def heapify(self, nums: List[int]) -> None:
        self.arr = [0] + nums
        for i in reversed(range(1, len(self.arr) // 2 +1)):
            self.bubbleDown(1)
        return None

    def bubbleDown(self, index):
        ans = self.arr[index]
        child=2*index
        while index*2<len(self.arr):
            if child+1 < len(self.arr) and self.arr[child+1]<self.arr[child]:
                child+=1
            if self.arr[child] >=self.arr[index]:
                return ans
            self.arr[child], self.arr[index] = self.arr[index], self.arr[child]
            index=child
            child = 2 * index
        self.index-=1
        