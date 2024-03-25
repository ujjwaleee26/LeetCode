# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        res=[]
        i=0
        ans=float('-inf')
        if root is None:
            return res
        q=deque()
        q.append(root)
        while q:
            qLen=len(q)
            level=[]
            for _ in range(qLen):
                node=q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                curr=sum(level)
                res.append(curr)
                i+=1
        if k>i:
            return -1
        res.sort(reverse=True)
        return res[k-1]
        res=[]
        i=0
        ans=float('-inf')
        if root is None:
            return res
        q=deque()
        q.append(root)
        while q:
            qLen=len(q)
            level=[]
            for _ in range(qLen):
                node=q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                curr=sum(level)
                res.append(curr)
                i+=1
        if k>i:
            return -1
        res.sort(reverse=True)
        return res[k-1]
        