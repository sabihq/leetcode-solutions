class Solution(object):
    def maxPathSum(self, root):
        self.maximum = float("-inf")

        def dfs(node):
            if not node:
                return 0

            # Maximum downward path from each child.
            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)

            # Best path that uses this node as the highest point.
            current_path = node.val + left_gain + right_gain
            self.maximum = max(self.maximum, current_path)

            # A path passed to the parent can use only one branch.
            return node.val + max(left_gain, right_gain)

        dfs(root)
        return self.maximum