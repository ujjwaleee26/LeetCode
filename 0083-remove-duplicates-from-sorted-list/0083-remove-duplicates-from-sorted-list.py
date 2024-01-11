# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        else:
            tempNode=head.next
            prevNode=head
            while tempNode:
                if tempNode.val == prevNode.val:
                    prevNode.next=tempNode.next
                    tempNode=tempNode.next
                else:
                    prevNode=tempNode
                    tempNode=tempNode.next
                    
            return head        