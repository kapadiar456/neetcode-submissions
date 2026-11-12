class Node:
    def __init__(self, val):
        self.next = None
        self.prev = None
        self.val = val


class Deque:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head


    def isEmpty(self) -> bool:
        if self.head.next ==self.tail:
            return True
        return False

    def append(self, value: int) -> None:
        newNode = Node(value)
        print(value)
        self.tail.prev.next = newNode
        newNode.prev = self.tail.prev

        self.tail.prev = newNode
        newNode.next = self.tail        

    def appendleft(self, value: int) -> None:
        newNode = Node(value)
        newNode.next = self.head.next
        self.head.next.prev = newNode
        self.head.next = newNode

    def pop(self) -> int:
        if self.tail.prev == self.head:
            return -1
        val = self.tail.prev.val
        self.tail.prev = self.tail.prev.prev
        self.tail.prev.next = self.tail
        return val
        
    def popleft(self) -> int:
        if self.head.next == self.tail:
            return -1
        val = self.head.next.val
        self.head.next = self.head.next.next
        self.head.next.prev = self.head
        return val
        
