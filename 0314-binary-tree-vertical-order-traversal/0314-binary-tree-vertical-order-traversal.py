from collections import defaultdict, deque
from typing import List

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        columns = defaultdict(list)
        queue = deque([(root, 0)])

        while queue:
            node, col = queue.popleft()
            columns[col].append(node.val)

            if node.left:
                queue.append((node.left, col - 1))

            if node.right:
                queue.append((node.right, col + 1))

        return [columns[col] for col in sorted(columns)]
