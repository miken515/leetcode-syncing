# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        prev = dummy

        while head and head.next:
            node1 = head
            node2 = head.next

            prev.next = node2
            node1.next = node2.next
            node2.next = node1

            prev = node1
            head = node1.next
        
        return dummy.next
