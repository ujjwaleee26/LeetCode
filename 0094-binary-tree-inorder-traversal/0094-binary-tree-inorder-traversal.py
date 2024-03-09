# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inList=[]
        if root is None:
            return inList
        inList.extend(self.inorderTraversal(root.left) or [])
        inList.append(root.val)
        inList.extend(self.inorderTraversal(root.right) or [])
        return inList
        