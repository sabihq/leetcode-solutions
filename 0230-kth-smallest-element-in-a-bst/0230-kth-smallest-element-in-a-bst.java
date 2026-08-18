class Solution {
    public int kthSmallest(TreeNode root, int k) {
        Stack<TreeNode> stack = new Stack<>();
        TreeNode current = root;

        while (current != null || !stack.isEmpty()) {

            // Go as far left as possible
            while (current != null) {
                stack.push(current);
                current = current.left;
            }

            // Smallest remaining node
            current = stack.pop();
            k--;

            if (k == 0) {
                return current.val;
            }

            // Check the right subtree
            current = current.right;
        }

        return -1;
    }
}