class Node(object):
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}

        # Dummy nodes marking both ends of the list
        self.left = Node()   # Least recently used side
        self.right = Node()  # Most recently used side

        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        """Remove a node from the linked list."""
        previous = node.prev
        following = node.next

        previous.next = following
        following.prev = previous

    def insert(self, node):
        """Insert a node at the most recently used side."""
        previous = self.right.prev

        previous.next = node
        node.prev = previous
        node.next = self.right
        self.right.prev = node

    def get(self, key):
        if key not in self.cache:
            return -1

        node = self.cache[key]

        # This key is now the most recently used
        self.remove(node)
        self.insert(node)

        return node.value

    def put(self, key, value):
        if key in self.cache:
            old_node = self.cache[key]
            self.remove(old_node)

        new_node = Node(key, value)
        self.cache[key] = new_node
        self.insert(new_node)

        if len(self.cache) > self.capacity:
            # Remove the least recently used node
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]