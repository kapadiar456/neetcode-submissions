# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:  
    def merge(self, list1, list2):
        newList = None
        while list1 and list2:
            if list1.val<=list2.val:
                if not newList:
                    newList = ListNode(list1.val)
                    head = newList
                    list1 = list1.next
                else:
                    newList.next = ListNode(list1.val)
                    list1 = list1.next
                    newList = newList.next
            else:
                if not newList:
                    newList = ListNode(list2.val)
                    head = newList
                    list2 = list2.next
                else:
                    newList.next = ListNode(list2.val)
                    list2 = list2.next
                    newList = newList.next

        if list1:
            newList.next = list1
        elif list2:
            newList.next = list2
        return head
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        for i in range(1, len(lists)):
            lists[i]= self.merge(lists[i], lists[i-1])
        if lists:
            return lists[-1]
        else:
            return None
