# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        l=0
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
                i+=1
                if curr>ans:
                    ans=curr
                    l=i
            
        return l