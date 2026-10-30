from typing import List

class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        pieces_needed = k + 1
        left = min(sweetness)
        right = sum(sweetness) // pieces_needed

        while left < right:
            mid = (left + right + 1) // 2

            pieces = 0
            current_sum = 0

            for value in sweetness:
                current_sum += value

                if current_sum >= mid:
                    pieces += 1
                    current_sum = 0

            if pieces >= pieces_needed:
                left = mid
            else:
                right = mid - 1

        return left