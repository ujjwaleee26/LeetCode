# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        else:
            list=[]
            tempNode=head
            rNode=head
            while tempNode:
                list.append(tempNode.val)
                tempNode=tempNode.next
            list.sort() 
            list.reverse()
            while rNode:
                rNode.val=list.pop()
                rNode=rNode.next
            return head    
        