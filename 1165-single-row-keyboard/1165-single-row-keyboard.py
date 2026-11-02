class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        positions = {char: i for i, char in enumerate(keyboard)}
        current = 0
        total = 0

        for char in word:
            target = positions[char]
            total += abs(target - current)
            current = target

        return total