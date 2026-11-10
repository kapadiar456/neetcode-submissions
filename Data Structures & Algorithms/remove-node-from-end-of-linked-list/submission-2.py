# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        h1 = head
        while h1:
            length+=1
            h1 = h1.next
        position = length - n 

        dummyHead = ListNode(-1, head)
        ptr = dummyHead
        length = 0
        h2 = head
        while dummyHead:
            if length == position:
                dummyHead.next = dummyHead.next.next
            dummyHead = dummyHead.next
            length +=1
        return ptr.next
