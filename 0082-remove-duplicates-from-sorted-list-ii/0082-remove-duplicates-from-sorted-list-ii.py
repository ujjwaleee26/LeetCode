# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy1=head
        list1=[]
        temp=200
        if head is None or head.next is None:
            return head
        else:
            prevNode=head
            tempNode=head.next
            while tempNode:
                if prevNode.val!=tempNode.val:
                    if temp != prevNode.val:
                         list1.append(prevNode.val)
                else:
                    temp=prevNode.val  
                prevNode=prevNode.next
                tempNode=tempNode.next
        if prevNode.val !=temp:
            list1.append(prevNode.val)
        list1.reverse() 
        if list1==[]:
            return None
        else:
            while list1 !=[]:
                dummy1.val=list1.pop()
                if list1==[]:
                    break
                dummy1=dummy1.next
            dummy1.next=None
            return head
        