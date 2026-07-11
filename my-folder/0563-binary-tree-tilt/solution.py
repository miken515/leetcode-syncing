# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        totalTilt = 0

        def dfs(node):
            nonlocal totalTilt
            if not node:
                return 0 
            
            leftNode = dfs(node.left)
            rightNode = dfs(node.right)
            tilt = abs(leftNode - rightNode)
            totalTilt += tilt

            return leftNode + rightNode + node.val

        dfs(root)
        return totalTilt
