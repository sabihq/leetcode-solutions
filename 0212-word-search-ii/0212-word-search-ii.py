class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        # Build a Trie from all words
        trie = {}

        for word in words:
            node = trie

            for letter in word:
                if letter not in node:
                    node[letter] = {}
                node = node[letter]

            node["$"] = word

        rows = len(board)
        cols = len(board[0])
        result = []

        def dfs(row, col, node):
            letter = board[row][col]

            if letter not in node:
                return

            next_node = node[letter]

            # A complete word was found
            if "$" in next_node:
                result.append(next_node.pop("$"))

            # Mark this cell as visited
            board[row][col] = "#"

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for row_change, col_change in directions:
                next_row = row + row_change
                next_col = col + col_change

                if (0 <= next_row < rows and
                    0 <= next_col < cols and
                    board[next_row][next_col] != "#"):

                    dfs(next_row, next_col, next_node)

            # Restore the cell for other searches
            board[row][col] = letter

            # Remove exhausted Trie branches
            if not next_node:
                node.pop(letter)

        for row in range(rows):
            for col in range(cols):
                dfs(row, col, trie)

        return result