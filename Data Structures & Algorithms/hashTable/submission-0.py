class Entry:
    def __init__(self, key:int, value:int):
        self.key = key
        self.val = value
class HashTable:
    
    def __init__(self, capacity: int):
        self.totalEntries = 0
        self.arr = [None]*capacity

    def insert(self, key: int, value: int) -> None:
        hashValue = key%len(self.arr)
        entry = Entry(key, value)
    
        
        if self.totalEntries+1 >= len(self.arr)//2:
            print("Key: ", key, ", ", self.totalEntries)
            self.resize()

        if self.arr[hashValue]==None:
            self.arr[hashValue] = entry
            self.totalEntries+=1
            return

        elif not self.arr[hashValue]== None and self.arr[hashValue].key == key:
            self.arr[hashValue].val = value
            return

        else:
            while not self.arr[hashValue]==None:
                if hashValue == len(self.arr):
                    hashValue=0
                hashValue+=1
            self.insert(key,value)
    
    def get(self, key: int) -> int:
        hashValue = key%len(self.arr)
        if self.arr[hashValue]==None:
            return -1
        else:
            return self.arr[hashValue].val


    def remove(self, key: int) -> bool:
        hashValue = key%len(self.arr)
        if self.arr[hashValue] == None:
            return False
        else:
            self.arr[hashValue] = None
            self.totalEntries-=1
            return True
    

    def getSize(self) -> int:
        return self.totalEntries

    def getCapacity(self) -> int:
        return len(self.arr)

    def resize(self) -> None:
        newArr = [None]*(len(self.arr)*2)
        temp = self.arr
        self.arr = newArr
        self.totalEntries=0
        for entry in temp:
            if not entry == None:
                self.insert(entry.key, entry.val)