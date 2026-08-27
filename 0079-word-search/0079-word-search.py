class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        rows = len(board)
        cols = len(board[0])

        def search(row, col, index):
            # Every character in the word was found
            if index == len(word):
                return True

            # Invalid position or incorrect character
            if (row < 0 or row >= rows or
                col < 0 or col >= cols or
                board[row][col] != word[index]):
                return False

            # Temporarily mark this cell as used
            letter = board[row][col]
            board[row][col] = "#"

            found = (
                search(row + 1, col, index + 1) or
                search(row - 1, col, index + 1) or
                search(row, col + 1, index + 1) or
                search(row, col - 1, index + 1)
            )

            # Restore the cell for other searches
            board[row][col] = letter

            return found

        # Try every cell as the starting position
        for row in range(rows):
            for col in range(cols):
                if search(row, col, 0):
                    return True

        return False
        