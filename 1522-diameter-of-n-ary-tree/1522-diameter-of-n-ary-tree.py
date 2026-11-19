class Solution:
    def diameter(self, root: 'Node') -> int:
        self.max_diameter = 0

        def dfs(node):
            if not node:
                return 0

            longest = 0
            second_longest = 0

            for child in node.children:
                depth = dfs(child) + 1

                if depth > longest:
                    second_longest = longest
                    longest = depth
                elif depth > second_longest:
                    second_longest = depth

            self.max_diameter = max(
                self.max_diameter,
                longest + second_longest
            )

            return longest

        dfs(root)
        return self.max_diameter