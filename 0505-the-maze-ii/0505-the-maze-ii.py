from typing import List
import heapq

class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        m, n = len(maze), len(maze[0])

        distances = [[float('inf')] * n for _ in range(m)]
        distances[start[0]][start[1]] = 0

        heap = [(0, start[0], start[1])]

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while heap:
            dist, row, col = heapq.heappop(heap)

            if dist > distances[row][col]:
                continue

            if [row, col] == destination:
                return dist

            for dr, dc in directions:
                r, c = row, col
                steps = 0

                while (
                    0 <= r + dr < m
                    and 0 <= c + dc < n
                    and maze[r + dr][c + dc] == 0
                ):
                    r += dr
                    c += dc
                    steps += 1

                new_dist = dist + steps

                if new_dist < distances[r][c]:
                    distances[r][c] = new_dist
                    heapq.heappush(heap, (new_dist, r, c))

        return -1