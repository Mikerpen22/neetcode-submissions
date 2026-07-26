class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 1. 建立 dummy node 指向 head，解決頭節點被刪除的邊界問題
        dummy = ListNode(0, head)
        fast = slow = dummy

        # 2. 讓 fast 先走 n 步，建立長度為 n 的間距
        for _ in range(n):
            fast = fast.next

        # 3. 兩指標同時推進，直到 fast 到達最後一個節點
        # 此時 slow 會精準停在「待刪除節點的前一個節點」
        while fast.next:
            fast = fast.next
            slow = slow.next

        # 4. 跨過倒數第 n 個節點（即 slow.next），完成刪除
        slow.next = slow.next.next

        return dummy.next