# Doubly linked list node.
# Store both key and value so we can remove the key
# from the hashmap in O(1) when evicting the LRU node.
class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        # HashMap: key -> node
        self.cache = {}

        # Dummy head/tail eliminate edge cases.
        #
        # head <-> MRU ... LRU <-> tail
        #
        # head.next: Most Recently Used
        # tail.prev: Least Recently Used
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

        self.capacity = capacity

    def _removeNodeFromList(self, node: Node) -> Node:
        # Remove a node by reconnecting its neighbors.
        prevNode = node.prev
        nextNode = node.next

        prevNode.next = nextNode
        nextNode.prev = prevNode

        return node

    def _insertToHead(self, node: Node) -> Node:
        # Insert immediately after dummy head.
        # The inserted node becomes the new MRU.
        first = self.head.next

        node.prev = self.head
        node.next = first

        self.head.next = node
        first.prev = node

        return node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        # Accessed node becomes MRU.
        node = self.cache[key]
        self._removeNodeFromList(node)
        self._insertToHead(node)

        return node.val

    def put(self, key: int, value: int) -> None:

        # Existing key:
        # 1. Update value.
        # 2. Move it to MRU.
        if key in self.cache:
            node = self.cache[key]
            node.val = value

            self._removeNodeFromList(node)
            self._insertToHead(node)

        else:
            # Create a new node.
            node = Node(key, value)

            # Add it to both the hashmap and linked list.
            self.cache[key] = node
            self._insertToHead(node)

            # If over capacity, remove the LRU node
            # (the node right before the dummy tail).
            if len(self.cache) > self.capacity:
                lru = self._removeNodeFromList(self.tail.prev)
                del self.cache[lru.key]