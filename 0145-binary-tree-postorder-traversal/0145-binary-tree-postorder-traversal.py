# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        postList=[]
        if root is None:
            return postList
        postList.extend(self.postorderTraversal(root.left) or [])
        postList.extend(self.postorderTraversal(root.right) or [])
        postList.append(root.val)
        return postList