# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head.next == None:
            return False
        tortoise = head
        hare = head
        while hare.next.next:
            hare = hare.next.next
            tortoise = tortoise.next
            if tortoise == hare:
                return True
        return False