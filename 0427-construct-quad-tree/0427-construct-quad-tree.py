class Solution:
    def construct(self, grid):
        def build(row, col, size):
            first_value = grid[row][col]
            same_value = True

            for r in range(row, row + size):
                for c in range(col, col + size):
                    if grid[r][c] != first_value:
                        same_value = False
                        break

                if not same_value:
                    break

            if same_value:
                return Node(first_value == 1, True)

            half = size // 2

            top_left = build(row, col, half)
            top_right = build(row, col + half, half)
            bottom_left = build(row + half, col, half)
            bottom_right = build(row + half, col + half, half)

            return Node(
                True,
                False,
                top_left,
                top_right,
                bottom_left,
                bottom_right
            )

        return build(0, 0, len(grid))