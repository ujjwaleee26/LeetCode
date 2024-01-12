# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tempNode=head
        prevNode=None
        while tempNode:
            nextNode=tempNode.next
            tempNode.next=prevNode
            prevNode=tempNode
            tempNode=nextNode
        return prevNode   
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tempNode=self.reverseList(head)
        rNode=tempNode
        prevNode=None
        carry=0
        while rNode:
            if rNode.val <=4:
                rNode.val=2*rNode.val + carry
                prevNode=rNode
                rNode=rNode.next
                carry=0
            else:
                rNode.val=int((2*rNode.val + carry)%10)
                carry=1
                prevNode=rNode
                rNode=rNode.next
        if carry==1:
            newNode=ListNode(carry)
            prevNode.next=newNode
        return self.reverseList(tempNode)    
        
            