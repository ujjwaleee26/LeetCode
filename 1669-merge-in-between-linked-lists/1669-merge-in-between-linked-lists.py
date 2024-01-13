# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        tempNode=list1
        prevNode=None
        rNode=list2
        while rNode.next is not None:
            rNode=rNode.next
        c=0
        while tempNode:
            if c==a:
                break
            else:
                prevNode=tempNode
                tempNode=tempNode.next
                c=c+1
        prevNode.next=list2 
        d=b-a
        while d:
            tempNode=tempNode.next
            d=d-1
        tempNode=tempNode.next
        while prevNode.next is not None:
            prevNode=prevNode.next
        prevNode.next=tempNode
        return list1
        