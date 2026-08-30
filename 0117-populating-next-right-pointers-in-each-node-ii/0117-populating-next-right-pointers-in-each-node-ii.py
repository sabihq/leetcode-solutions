class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        current_level = root

        while current_level:
            dummy = Node(0)
            tail = dummy

            # Move across the current level using next pointers
            current = current_level

            while current:
                if current.left:
                    tail.next = current.left
                    tail = tail.next

                if current.right:
                    tail.next = current.right
                    tail = tail.next

                current = current.next

            # First node of the next level
            current_level = dummy.next

        return root