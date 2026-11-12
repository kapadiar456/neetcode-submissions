# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        pointerToHead = head
        while head.next:
            tempHead = head.next
            head.next = prev
            prev = tempHead
        return tempHead.next
        