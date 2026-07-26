# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        slow, fast = head, head
        while fast and n-1 > 0:
            fast = fast.next
            n -= 1
        
        prev = None
        while fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next
        
        # slow is the nth node from the end of the list, readjust pointers around it
        if prev:
            prev.next = slow.next
        else:
            head = head.next

        return head

        
