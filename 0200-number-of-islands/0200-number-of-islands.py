class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        def dfs(row, col):
            # Stop if out of bounds or not land
            if (
                row < 0 or row >= rows or
                col < 0 or col >= cols or
                grid[row][col] != "1"
            ):
                return

            # Mark this land as visited
            grid[row][col] = "0"

            # Visit connected land
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    islands += 1
                    dfs(row, col)

        return islands