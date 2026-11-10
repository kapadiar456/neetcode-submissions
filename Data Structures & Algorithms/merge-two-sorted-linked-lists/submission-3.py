
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode(-1)
        pointerToDummy = dummyNode
        while list1 and list2:
            if list1.val <= list2.val:
                dummyNode.next = list1
                temp = list1.next
                list1.next = list2
                list1 = temp
            else:
                dummyNode.next = list2
                temp = list2.next
                list2.next = list1
                list2 = temp
            dummyNode = dummyNode.next
        if list2:
            dummyNode.next = list2
        if list1:
            dummyNode.next = list1
        return pointerToDummy.next