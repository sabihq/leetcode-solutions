class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        closest = root.val

        while root:
            if (abs(root.val - target) < abs(closest - target) or
                (abs(root.val - target) == abs(closest - target)
                 and root.val < closest)):
                closest = root.val

            if target < root.val:
                root = root.left
            elif target > root.val:
                root = root.right
            else:
                return root.val

        return closest
