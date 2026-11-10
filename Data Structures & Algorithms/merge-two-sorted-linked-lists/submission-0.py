# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode(-1)
        head = dummyNode
        while list1 and list2:
            if list1.val<=list2.val:
                dummyNode.next = list1
                dummyNode = dummyNode.next
                list1 = list1.next
            elif list2.val < list1.val:
                dummyNode.next = list2
                dummyNode = dummyNode.next
                list2 = list2.next
        while list1:
            dummyNode.next = list1
            dummyNode = dummyNode.next
            list1 = list1.next
        while list2:
            dummyNode.next = list2
            dummyNode = dummyNode.next
            list2 = list2.next
        return head.next