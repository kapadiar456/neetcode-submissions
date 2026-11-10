# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyNode = ListNode(-1)
        headPointer = dummyNode
        dummyNode.next = head
        length = 0
        while head:
            head = head.next
            length+=1
        print(length)
        index = length - n
        count = 0
        while dummyNode:
            if count == index:
                dummyNode.next = dummyNode.next.next
            dummyNode = dummyNode.next
            count+=1
        return headPointer.next
        

