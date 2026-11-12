# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        newNode = ListNode(-1)
        ptr = newNode
        for i in range(1, len(lists)):
            l1 = lists[i-1]
            l2 = lists[i-2]
            newNode.next = self.merge(l1, l2).next
        return ptr.next


    def merge(self, list1, list2):
        newNode = ListNode(-1)
        ptr = newNode
        while list1 and list2:
            if list1.val <= list2.val:
                newNode.next = list1
                newNode = newNode.next
                list1 = list1.next
            else:
                newNode.next = list2
                newNode = newNode.next
                list2 = list2.next
        if list1:
            newNode.next = list1
        
        if list2:
            newNode.next = list2
        return ptr
                