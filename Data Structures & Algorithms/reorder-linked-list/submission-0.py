from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        if not head or not head.next:
            return

        # Step 1: 找到前半段的最後一個節點
        #
        # fast 從 head.next 開始：
        # - 奇數長度時，slow 停在真正中點
        # - 偶數長度時，slow 停在第一個中點
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # second 是後半段的第一個節點
        second = slow.next

        # 將前後兩段切開，否則後面 merge 時可能形成 cycle
        slow.next = None

        # Step 2: 反轉後半段
        prev = None
        curr = second

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # prev 現在是反轉後的後半段頭節點
        second = prev

        # Step 3: 交錯合併兩段
        first = head

        while second:
            first_next = first.next
            second_next = second.next

            first.next = second
            second.next = first_next

            first = first_next
            second = second_next