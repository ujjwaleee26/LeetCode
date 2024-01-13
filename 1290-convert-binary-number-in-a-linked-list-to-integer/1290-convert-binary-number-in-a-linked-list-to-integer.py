# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self,head:ListNode)-> ListNode:
        prevNode=None
        tempNode=head
        while tempNode:
            nextNode=tempNode.next
            tempNode.next=prevNode
            prevNode=tempNode
            tempNode=nextNode
        return prevNode 
    def getDecimalValue(self, head: ListNode) -> int:
        newHead=self.reverseList(head)
        tempNode=newHead
        i=0
        s=0
        while tempNode:
            s=s+ ( pow(2,i) * tempNode.val)
            i=i+1
            tempNode=tempNode.next
        return s    