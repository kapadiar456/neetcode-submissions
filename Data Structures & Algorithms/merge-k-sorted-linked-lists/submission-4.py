# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists)==0:
            return None
        return self.divide(lists, 0, len(lists)-1)
    def divide(self, lists, l, r):
        if l > r:
            return None
        if l == r:
            return lists[l]

        m = l + (r-l) // 2
        left = self.divide(lists, l, m)
        right = self.divide(lists, m+1, r)
        return self.merge(left, right)



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
        return ptr.next
                