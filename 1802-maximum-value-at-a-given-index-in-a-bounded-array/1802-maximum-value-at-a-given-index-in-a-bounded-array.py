class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def side_sum(peak: int, length: int) -> int:
            # Descend from peak - 1, stopping at 1.
            count = min(length, peak - 1)
            descending = count * (2 * peak - count - 1) // 2
            return descending + (length - count)

        def feasible(peak: int) -> bool:
            total = (
                peak
                + side_sum(peak, index)
                + side_sum(peak, n - index - 1)
            )
            return total <= maxSum

        low, high = 1, maxSum - n + 1

        while low < high:
            mid = (low + high + 1) // 2
            if feasible(mid):
                low = mid
            else:
                high = mid - 1

        return low