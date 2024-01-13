# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prevNode=None
        tempNode=head
        while tempNode:
            nextNode=tempNode.next
            tempNode.next=prevNode
            prevNode=tempNode
            tempNode=nextNode
        return prevNode  
    def pairSum(self, head: Optional[ListNode]) -> int:
        prevNode=head
        tempNode=head
        supportNode=head
        useNode1=None
        while tempNode and tempNode.next:
            useNode1=prevNode
            prevNode=prevNode.next
            tempNode=tempNode.next.next
        useNode1.next=None
        useNode2=self.reverseList(prevNode)
        list=[]
        while useNode2:
            list.append(useNode2.val + supportNode.val)
            supportNode=supportNode.next
            useNode2=useNode2.next
        list.sort()
        return list.pop()
            
        