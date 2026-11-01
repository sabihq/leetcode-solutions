from typing import List


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_value = arrays[0][0]
        max_value = arrays[0][-1]
        answer = 0

        for i in range(1, len(arrays)):
            current_min = arrays[i][0]
            current_max = arrays[i][-1]

            answer = max(
                answer,
                abs(current_max - min_value),
                abs(current_min - max_value),
            )

            min_value = min(min_value, current_min)
            max_value = max(max_value, current_max)

        return answer