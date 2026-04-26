class Node:
    def __init__(self, val=None):
        self.val = val
        self.children = []
        self.is_end = False

class PrefixTree:

    def __init__(self):
        self.root = Node()  # dummy root

    def insert(self, word: str) -> None:
        current_node = self.root
        for c in word:
            found = False
            for child in current_node.children:
                if child.val == c:
                    # this child node match this char
                    # move current to this child
                    # then move on to next char
                    current_node = child
                    found = True
                    break
            if not found:
                # did not match, we need to "create" node
                # then we move current to this child
                # then move on to next char
                next_node = Node(val=c)
                current_node.children.append(next_node)
                current_node = next_node
        current_node.is_end = True

    def search(self, word: str) -> bool:
        current_node = self.root
        for c in word:
            has_val = False
            for child in current_node.children:
                if c == child.val:
                    current_node = child
                    has_val = True
                    break

            if not has_val:
                return False
                    
        if current_node.is_end:   
            return True
        else: 
            return False

    def startsWith(self, prefix: str) -> bool:
        current_node = self.root
        for c in prefix:
            has_val = False
            for child in current_node.children:
                if c == child.val:
                    current_node = child
                    has_val = True
                    break

            if not has_val:
                return False
                    
                
        return True

        
        