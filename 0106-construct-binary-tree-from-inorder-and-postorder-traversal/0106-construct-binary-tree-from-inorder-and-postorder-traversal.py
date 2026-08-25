class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        inorder_index = {}

        for i, value in enumerate(inorder):
            inorder_index[value] = i

        postorder_index = [len(postorder) - 1]

        def build(left, right):
            if left > right:
                return None

            # Last remaining postorder value is the root
            root_value = postorder[postorder_index[0]]
            postorder_index[0] -= 1

            root = TreeNode(root_value)
            middle = inorder_index[root_value]

            # Build right first because postorder is read backward
            root.right = build(middle + 1, right)
            root.left = build(left, middle - 1)

            return root

        return build(0, len(inorder) - 1)