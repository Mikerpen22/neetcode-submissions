# double link list
class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        # closer to head = MRU; closer to tail = LRU
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity

    def _removeNodeFromList(self, n: Node) -> Node:
        nextNode = n.next
        prevNode = n.prev
        n.prev.next = nextNode
        n.next.prev = prevNode
        return n

    def _insertToHead(self, n: Node) -> Node:
        curHead = self.head.next

        n.next = curHead
        n.prev = self.head
        curHead.prev = n
        self.head.next = n
        
        return self.head.next

    def get(self, key: int) -> int:
        if not key in self.cache:
            return -1
        else:
            ret = self.cache[key].val
            # this key is accessed, so it has to be moved to MRU
            n = self._removeNodeFromList(self.cache[key])
            _ = self._insertToHead(n)

            return ret

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            n = self._removeNodeFromList(node)
            self._insertToHead(n)
            self.cache[key] = n

        else:
            self.cache[key] = Node(key, value)
            if len(self.cache) > self.capacity:
                # over cap, remove lru (= self.tail.prev)
                n = self._removeNodeFromList(self.tail.prev)
                del self.cache[n.key]
            # update current node as MRU
            self._insertToHead(self.cache[key])
