class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.arr = [0] * self.capacity


    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i]=n

    def pushback(self, n: int) -> None:
        if self.capacity == self.length:
            self.resize()
        self.arr[self.length]=n
        self.length+=1


    def popback(self) -> int:
        myVal = self.arr[self.length-1]
        self.arr[self.length-1]=0
        self.length-=1
        return myVal
 

    def resize(self) -> None:
        self.capacity = self.capacity * 2
        arr2 = [0] * self.capacity
        for x in range(len(self.arr)):
            arr2[x]=self.arr[x]
        self.arr = arr2

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity