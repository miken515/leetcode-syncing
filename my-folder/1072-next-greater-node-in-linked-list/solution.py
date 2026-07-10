# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        res = []
        stack = [] #count and head val
        cnt = 0

        while head:
            res.append(0)

            while stack and head.val > stack[-1][1]:
                curIdx, val = stack.pop()
                res[curIdx] = head.val
            
            stack.append([cnt, head.val])
            cnt += 1
            head = head.next
        
        return res
