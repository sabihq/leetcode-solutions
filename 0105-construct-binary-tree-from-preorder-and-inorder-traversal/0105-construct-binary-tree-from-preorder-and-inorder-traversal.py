class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        inorder_index = {}

        for i, value in enumerate(inorder):
            inorder_index[value] = i

        # List allows the nested function to update the index in Python 2
        preorder_index = [0]

        def build(left, right):
            if left > right:
                return None

            root_value = preorder[preorder_index[0]]
            preorder_index[0] += 1

            root = TreeNode(root_value)
            middle = inorder_index[root_value]

            root.left = build(left, middle - 1)
            root.right = build(middle + 1, right)

            return root

        return build(0, len(inorder) - 1)