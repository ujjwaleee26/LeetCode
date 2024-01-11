# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy1=head
        dummy2=head
        list=[]
        j=0
        while dummy1:
            if j>= (left-1):
                list.append(dummy1.val)
                j+=1
                if j==right:
                    break
            else:
                j+=1
            dummy1=dummy1.next
        i=0
        while dummy2:
            if i>= (left-1):
                dummy2.val=list.pop()
                i+=1
                if i==right:
                    break
            else:
                i+=1
            dummy2=dummy2.next
        return head    