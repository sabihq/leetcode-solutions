class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        rows = len(board)
        cols = len(board[0])

        def dfs(row, col):
            if (
                row < 0 or row >= rows or
                col < 0 or col >= cols or
                board[row][col] != "O"
            ):
                return

            # Mark border-connected O's as safe
            board[row][col] = "S"

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        # Check left and right borders
        for row in range(rows):
            dfs(row, 0)
            dfs(row, cols - 1)

        # Check top and bottom borders
        for col in range(cols):
            dfs(0, col)
            dfs(rows - 1, col)

        # Capture surrounded regions
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "S":
                    board[row][col] = "O"