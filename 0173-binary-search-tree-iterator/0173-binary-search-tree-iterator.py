class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: Optional[TreeNode]
        """
        self.stack = []
        self._pushLeft(root)

    def _pushLeft(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self):
        """
        :rtype: int
        """
        node = self.stack.pop()

        if node.right:
            self._pushLeft(node.right)

        return node.val

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) > 0