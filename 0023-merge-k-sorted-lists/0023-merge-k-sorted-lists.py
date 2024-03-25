# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n=len(lists)
        if lists ==[] or (lists[0] is None and n==1):
            return None
        l=[]
        for x in lists:
            if x is not None:
                while x:
                    l.append(x.val)
                    x=x.next
        l.sort(reverse=True)
        if l ==[]:
            return None
        i=ListNode(l.pop())
        res=i
        while l!=[]:
            h=ListNode(l.pop())
            i.next=h
            i=i.next
        return res
        