# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        freq = {}

        def dfs(node):
            if not node:
                return

            if node.val not in freq:
                freq[node.val] = 1
            else:
                freq[node.val] += 1

            dfs(node.left)
            dfs(node.right)

        dfs(root)
        print(freq.values())

        maxFreq = max(freq.values())

        res = []
        for val, count in freq.items():
            print(val, count)
            if count == maxFreq:
                res.append(val)

        return res
