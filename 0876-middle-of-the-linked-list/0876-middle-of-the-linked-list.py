# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prevNode=head
        tempNode=head
        while tempNode and tempNode.next:
            prevNode=prevNode.next
            tempNode=tempNode.next.next
        return prevNode    
        