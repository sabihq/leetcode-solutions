from collections import deque
from typing import List

class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.width = width
        self.height = height
        self.food = food
        self.score = 0
        self.game_over = False

        self.snake = deque([(0, 0)])
        self.occupied = {(0, 0)}

        self.directions = {
            "U": (-1, 0),
            "D": (1, 0),
            "L": (0, -1),
            "R": (0, 1)
        }

    def move(self, direction: str) -> int:
        if self.game_over:
            return -1

        row, col = self.snake[0]
        dr, dc = self.directions[direction]

        nr, nc = row + dr, col + dc
        new_head = (nr, nc)

        # Check wall collision
        if not (0 <= nr < self.height and 0 <= nc < self.width):
            self.game_over = True
            return -1

        # Check if the snake eats food
        eats_food = (
            self.score < len(self.food)
            and [nr, nc] == self.food[self.score]
        )

        if eats_food:
            self.score += 1
        else:
            # Remove the tail before checking body collision
            tail = self.snake.pop()
            self.occupied.remove(tail)

        # Check body collision
        if new_head in self.occupied:
            self.game_over = True
            return -1

        # Add the new head
        self.snake.appendleft(new_head)
        self.occupied.add(new_head)

        return self.score