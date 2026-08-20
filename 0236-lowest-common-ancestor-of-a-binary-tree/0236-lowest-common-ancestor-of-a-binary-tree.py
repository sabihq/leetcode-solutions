class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        # Base case:
        # If we reach the end, or find p or q, return that node.
        if root is None or root == p or root == q:
            return root

        # Search for p and q in the left and right subtrees.
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # If p and q were found on different sides,
        # the current root is their lowest common ancestor.
        if left is not None and right is not None:
            return root

        # Otherwise, return whichever side found p or q.
        return left if left is not None else right