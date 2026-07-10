# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def helper(node, curMax, curMin):
            if not node:
                return curMax - curMin
            
            curMax = max(curMax, node.val)
            curMin = min(curMin, node.val)

            left = helper(node.left, curMax, curMin)
            right = helper(node.right, curMax, curMin)

            return max(left, right)

        return helper(root, root.val, root.val)
