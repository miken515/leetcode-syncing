# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        q = deque([root])

        while q and q[0] is not None:
            node = q.popleft()
            q.append(node.left)
            q.append(node.right)

        while q and q[0] is None:
            q.popleft()
            
        return not bool(q)
