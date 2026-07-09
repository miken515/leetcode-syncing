# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isSubPath(self, head, root):
        """
        :type head: Optional[ListNode]
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        def dfs(node, head):
            if head is None:
                return True
            if node is None:
                return False

            if node.val != head.val:
                return False

            return (dfs(node.left, head.next) or
                    dfs(node.right, head.next))

        def checkPaths(node):
            if node is None:
                return False

            return (dfs(node, head) or
                    checkPaths(node.left) or
                    checkPaths(node.right))

        return checkPaths(root)

