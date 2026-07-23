# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prevNode = None

        while head:
            nextNode = head.next    # 先存下一個node, 我之後需要拿來更新current node
            head.next = prevNode    # 修正current node
            prevNode = head         # 更新prevnode
            head = nextNode         # 更新current node
            

        return prevNode
