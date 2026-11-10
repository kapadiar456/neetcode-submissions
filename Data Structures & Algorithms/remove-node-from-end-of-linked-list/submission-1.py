# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyNode = ListNode(-1, head)
        pointerToDummy = dummyNode
        indexNode = head
        currNode = head
        length = 1
        while indexNode.next:
            indexNode = indexNode.next
            length+=1
        index = length-n
        print(index)
        while index>0:
            dummyNode = dummyNode.next
            index -=1
        if index == 0:
            dummyNode.next = dummyNode.next.next
        return pointerToDummy.next
        

