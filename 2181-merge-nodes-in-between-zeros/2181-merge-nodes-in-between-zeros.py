# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tempNode=head
        rNode=head
        prevNode=None
        s=0
        while tempNode:
            if tempNode.val==0:
                if s==0:
                    tempNode=tempNode.next
                    continue
                else:
                    rNode.val=s
                    s=0
                    prevNode=rNode
                    rNode=rNode.next
                    tempNode=tempNode.next
            else:
                s=s+tempNode.val
                tempNode=tempNode.next
        prevNode.next=None
        return head
        