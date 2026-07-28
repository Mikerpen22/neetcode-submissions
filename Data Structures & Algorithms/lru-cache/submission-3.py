class Node:
    """雙向鏈結串列節點：同時記錄 key 與 val，以便刪除 LRU 時能反查 Map"""
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.map = {}  # key -> Node（提供 O(1) 查找）
        
        # 建立哨兵節點 (Dummy Nodes)，省去檢查 self.head / self.tail 是否為 None 的邏輯
        self.head = Node()  # 靠近 head.next 的是 MRU (最新)
        self.tail = Node()  # 靠近 tail.prev 的是 LRU (最舊)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node) -> None:
        """從雙向鏈結串列中拔除指定節點：O(1)"""
        prev_node, next_node = node.prev, node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _insert_front(self, node: Node) -> None:
        """將節點插到頭部 (head 之後)，標記為最新使用 (MRU)：O(1)"""
        first_node = self.head.next  # 原本的最前端節點
        
        # 1. 綁定新節點的兩側
        node.prev = self.head
        node.next = first_node
        
        # 2. 更新舊有節點的指標
        self.head.next = node
        first_node.prev = node

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        
        # 存在 -> 刷新使用順序 (先拔除，再插回最前端)
        node = self.map[key]
        self._remove(node)
        self._insert_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        # 1. 若 key 已存在 -> 刪除舊節點（舊位置）
        if key in self.map:
            self._remove(self.map[key])
        
        # 2. 建立新節點並插入頭部（更新 Map 與 DLL）
        node = Node(key, value)
        self.map[key] = node
        self._insert_front(node)
        
        # 3. 超過容量 -> 剔除 tail.prev (LRU 節點)
        if len(self.map) > self.cap:
            lru_node = self.tail.prev
            self._remove(lru_node)
            del self.map[lru_node.key]  # 利用 Node 內存的 key 精確從 Map 刪除