class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None
        """
        current = root

        while current:
            if current.left:
                # Find the rightmost node of the left subtree
                predecessor = current.left

                while predecessor.right:
                    predecessor = predecessor.right

                # Attach the original right subtree
                predecessor.right = current.right

                # Move the left subtree to the right
                current.right = current.left
                current.left = None

            current = current.right