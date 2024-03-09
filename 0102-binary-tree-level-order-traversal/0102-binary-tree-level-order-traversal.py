# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result=[]
        if root is None :
            return result
        queue = deque([root])

        while queue:
            level_size = len(queue)
            current_level = []
            for _ in range(level_size):
                    node = queue.popleft()
                    current_level.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            result.append(current_level)

        return result
        
        
        