class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        def build(left, right):
            if left > right:
                return None

            middle = (left + right) // 2
            root = TreeNode(nums[middle])

            root.left = build(left, middle - 1)
            root.right = build(middle + 1, right)

            return root

        return build(0, len(nums) - 1)