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
        if self.index<=1:
            return -1

        if self.index==2:
            self.index-=1
            return self.arr.pop()
        
        ans=self.arr[1]

        for val in self.arr:
            print("Val: ", val)
        self.arr[1] = self.arr.pop()
        j = 1
        while (j*2)+1<len(self.arr):
            #Both are smaller
            if self.arr[j*2]<self.arr[j] and self.arr[(j*2)+1]<self.arr[j]:
                if self.arr[(j*2)+1] > self.arr[j*2]:   
                    temp = self.arr[j*2]
                    self.arr[j*2] = self.arr[j]
                    self.arr[j] = temp
                    j = j*2
                else:
                    temp = self.arr[(j*2)+1]
                    self.arr[(j*2)+1] = self.arr[j]
                    self.arr[j] = temp
                    j = (j*2)+1
            #Second is if right is larger
            elif self.arr[j*2]>self.arr[(j*2)+1]:
                temp = self.arr[(j*2)+1]
                self.arr[(j*2)+1] = self.arr[j]
                self.arr[j] = temp
                j = (j*2)+1
            #Third is if left is larger
            elif self.arr[j*2]<self.arr[(j*2)+1]:
                temp = self.arr[j*2]
                self.arr[j*2] = self.arr[j]
                self.arr[j] = temp
                j = j*2
            #In right place
            else:
                break
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
        