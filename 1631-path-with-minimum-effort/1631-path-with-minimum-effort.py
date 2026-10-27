from typing import List
import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])

        # effort[r][c] is the smallest effort found to reach (r, c).
        effort = [[float("inf")] * cols for _ in range(rows)]
        effort[0][0] = 0

        # Each entry is (effort, row, column).
        heap = [(0, 0, 0)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while heap:
            current_effort, row, col = heapq.heappop(heap)

            if current_effort > effort[row][col]:
                continue

            if row == rows - 1 and col == cols - 1:
                return current_effort

            for dr, dc in directions:
                next_row, next_col = row + dr, col + dc

                if 0 <= next_row < rows and 0 <= next_col < cols:
                    difference = abs(
                        heights[row][col] - heights[next_row][next_col]
                    )
                    next_effort = max(current_effort, difference)

                    if next_effort < effort[next_row][next_col]:
                        effort[next_row][next_col] = next_effort
                        heapq.heappush(
                            heap, (next_effort, next_row, next_col)
                        )