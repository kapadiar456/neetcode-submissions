
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            head = list2
        else:
            head = list1
        while list1 and list2:
            if list1.val <= list2.val:
                temp = list1.next
                list1.next = list2
                list1 = temp
            else:
                temp = list2.next
                list2.next = list1
                list2 = temp
        while list2:
            if list2.next == None:
                list2.next = list1
            list2 = list2.next
        while list1:
            if list1.next == None:
                list1.next = list2
            list1 = list1.next
        return head