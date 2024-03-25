# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        i=1
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
                if i%2 ==0:
                    level.reverse()
                    res.append(level)
                    i+=1
                else:
                    res.append(level)
                    i+=1
        return res
        