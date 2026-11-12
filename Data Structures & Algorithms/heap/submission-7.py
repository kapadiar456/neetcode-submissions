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

        for val in self.arr:
            print("Val: ", val)
        self.arr[1] = self.arr.pop()
        i = 1
        while (i*2)+1<len(self.arr):
            if (2 * i + 1 < len(self.arr) and self.arr[2 * i + 1] < self.arr[2 * i] and self.arr[i] > self.arr[2 * i + 1]):
            # Swap right child
                tmp = self.arr[i]
                self.arr[i] = self.arr[2 * i + 1]
                self.arr[2 * i + 1] = tmp
                i = 2 * i + 1
            elif self.arr[i] > self.arr[2 * i]:
                # Swap left child
                tmp = self.arr[i]
                self.arr[i] = self.arr[2 * i]
                self.arr[2 * i] = tmp
                i = 2 * i
            self.index-=1
        return ans

    def top(self) -> int:
        if self.index == 1:
            return -1
        else:
            return self.arr[1]

    def heapify(self, nums: List[int]) -> None:
        for num in nums:
            self.push(num)
        return None
        