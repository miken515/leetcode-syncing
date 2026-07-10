# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        first = head
        
        length = 0

        # Getting total length of nodes
        while first is not None:
            length += 1
            first = first.next
        
        #Subtracting n to find which element to remove
        length -= n
        first = dummy
        while length > 0:
            length -= 1
            first = first.next
        
        first.next = first.next.next
        return dummy.next
