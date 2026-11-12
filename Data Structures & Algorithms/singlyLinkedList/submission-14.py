class Node:
    def __init__(self, val, nextNode):
        self.value = val
        self.next = nextNode

class LinkedList:
    
    def __init__(self):
        self.Head = None
        self.Tail = None

    def get(self, index: int) -> int:
        count = 0 
        cur=self.Head
        while cur:
            if cur==None:
                return -1
            elif count==index:
                return cur.Value
            else:
                return -1
            cur=cur.next
            count+=1

    def insertHead(self, val: int) -> None:
        if self.Head==None:
            newHead = Node(val, None)
            self.Head=newHead
            self.Tail=newHead
        else:
            newHead = Node(val, self.Head)
            self.Head=newHead


    def insertTail(self, val: int) -> None:
        cur = self.Head
        if self.Head==None:
            self.Head==Node(val, None)
            self.Tail = self.Head
            return

        elif self.Head==self.Tail:
            self.Head.next = Node(val, None)
            self.Tail = self.Head.next
            return
        else:
            while cur.next:
                if cur.next==None:
                    cur.next = Node(val, None)
                    break
                cur = cur.next

    def remove(self, index: int) -> bool:
        cur=self.Head
        count=0
        if index==0:
            self.Head=self.Head.next
            return True
        while cur.next:
            if index==count+1:
                cur.next=cur.next.next
                if cur.next==None:
                    self.Tail=cur.next
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
