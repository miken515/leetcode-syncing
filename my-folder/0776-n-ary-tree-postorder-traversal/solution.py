"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        if not root:
            return res

        def dfs(node, postOrderList):
            if not node:
                return None
            
            for child in node.children:
                dfs(child, postOrderList)
            
            
            postOrderList.append(node.val)
        
        dfs(root, res)
        return res
