# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        prev = None
        h1 = head
        temp = None
        length = 1
        tempHead = head
        while tempHead.next:
            tempHead = tempHead.next
            length+=1
        print(length)
        half = (length+1) // 2
        count = 0
        newHead = h1
        newH1 = None
        prevNode = None
        while h1:
            if count==half:
                newH1 = h1
                prevNode.next = None
                break
            prevNode = h1
            h1 = h1.next
            count+=1
        newH1 = h1
        while newH1:
            temp = newH1.next
            newH1.next = prev
            prev = newH1
            newH1 = temp
        list1 = newHead
        list2 = prev
        x = None
        y = None
        
        while list1 and list2:
            x = list1.next
            list1.next = list2
            y = list2.next
            list2.next = x
            list1 = x
            list2 = y

        if list2:
            list1.next = list2

            