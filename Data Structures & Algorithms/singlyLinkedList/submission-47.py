class Node:
    def __init__(self, val, nextNode):
        self.value = val
        self.next = nextNode

class LinkedList:
    
    def __init__(self):
        self.Head = None
        self.Tail = None

    def get(self, index: int) -> int:
        cur=self.Head
        count=0
        if cur is None:
            return -1
        while cur:
            if index==count:
                return cur.value
            count+=1
            cur=cur.next
            #print(cur.value)
        return -1


    def insertHead(self, val: int) -> None:
        if self.Head==None:
            newHead = Node(val, None)
            self.Head = newHead
            self.Tail = newHead
        else:
            newHead = Node(val, self.Head)
            self.Head = newHead


    def insertTail(self, val: int) -> None:
        if self.Head == None:
            self.Head = Node(val, None)
            self.Tail = self.Head
            return

        elif self.Head==self.Tail:
            self.Head.next = Node(val, None)
            self.Tail = self.Head.next
            return
        else:
            cur=self.Head
            while cur.next:
                cur=cur.next
            cur.next = Node(val, None)
            self.Tail = cur.next


    def remove(self, index: int) -> bool:
        cur = self.Head
        count = 0
        if cur == None:
            return False

        if index==count and cur.next==None:
            self.Head=None
            self.Tail=None
            return True

        while cur:
            if index-1==count and cur.next.next==None:
                cur.next=None
                self.Tail = cur
                return True
            if index-1==count:
                cur.next = cur.next.next
                return True
            cur=cur.next
            count+=1
        return False
        
                
    def getValues(self) -> List[int]:
        values = []
        cur = self.Head
        while cur:
            values.append(cur.value)
            cur = cur.next
        return values
