# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        prelist = []
        if root is None:
            return prelist  # Return an empty list if the root is None

        prelist.append(root.val)
        prelist.extend(self.preorderTraversal(root.left) or [])  # Handle None left subtree
        prelist.extend(self.preorderTraversal(root.right) or [])  # Handle None right subtree

        return prelist
        