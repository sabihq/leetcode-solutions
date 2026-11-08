class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        m, n = len(board), len(board[0])

        while True:
            crush = set()

            # Check horizontal matches
            for i in range(m):
                for j in range(n - 2):
                    if board[i][j] != 0 and (
                        board[i][j] == board[i][j + 1] == board[i][j + 2]
                    ):
                        crush.update([(i, j), (i, j + 1), (i, j + 2)])

            # Check vertical matches
            for i in range(m - 2):
                for j in range(n):
                    if board[i][j] != 0 and (
                        board[i][j] == board[i + 1][j] == board[i + 2][j]
                    ):
                        crush.update([(i, j), (i + 1, j), (i + 2, j)])

            # Board is stable
            if not crush:
                return board

            # Crush candies
            for i, j in crush:
                board[i][j] = 0

            # Drop candies down
            for j in range(n):
                write = m - 1

                for i in range(m - 1, -1, -1):
                    if board[i][j] != 0:
                        board[write][j] = board[i][j]
                        write -= 1

                # Fill remaining spaces with zeros
                for i in range(write, -1, -1):
                    board[i][j] = 0