from typing import List

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        # Each of the first n - 1 rides takes at least one hour,
        # and the final ride takes a positive amount of time.
        if hour <= len(dist) - 1:
            return -1

        def can_arrive(speed: int) -> bool:
            time = 0

            for distance in dist[:-1]:
                time += (distance + speed - 1) // speed

            time += dist[-1] / speed
            return time <= hour

        left, right = 1, 10**7

        while left < right:
            mid = (left + right) // 2

            if can_arrive(mid):
                right = mid
            else:
                left = mid + 1

        return left if can_arrive(left) else -1