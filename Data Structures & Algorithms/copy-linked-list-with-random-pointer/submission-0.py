class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # Hash Map: key 是原節點，value 是複製出來的新節點
        old_to_new = {}

        # 階段 1：只複製節點本體（val），不接任何指標，並存入 Hash Map
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next

        # 階段 2：重新遍歷原鏈表，利用 Hash Map 連接 next 和 random 指標
        curr = head
        while curr:
            # 取出當前原節點對應的新節點
            copy_node = old_to_new[curr]
            
            # 連接 next 指標 (如果 curr.next 是 None，Get 出來也是 None)
            copy_node.next = old_to_new.get(curr.next)
            
            # 連接 random 指標
            copy_node.random = old_to_new.get(curr.random)
            
            curr = curr.next

        # 回傳頭節點對應的新節點
        return old_to_new[head]