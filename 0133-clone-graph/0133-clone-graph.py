class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None

        clones = {}

        def dfs(current):
            # If already cloned, return the existing copy
            if current in clones:
                return clones[current]

            # Create a copy of the current node
            copy = Node(current.val)
            clones[current] = copy

            # Clone all neighbors
            for neighbor in current.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy

        return dfs(node)