# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dummy = tail = TreeNode()

        while root:
            if root.left:
                pred = root.left
                while pred.right:
                    pred = pred.right
                
                pred.right = root
                left = root.left
                root.left = None
                root = left
            else:
                tail.right = tail = root
                root = root.right
        
        return dummy.right
