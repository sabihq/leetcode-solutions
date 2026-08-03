class Solution:
    def merge(self, intervals):
        # Sort intervals by their starting value
        intervals.sort(key=lambda interval: interval[0])

        merged = []

        for current in intervals:
            # No intervals yet, or there is no overlap
            if not merged or current[0] > merged[-1][1]:
                merged.append(current)
            else:
                # Overlap found, so extend the previous interval
                merged[-1][1] = max(merged[-1][1], current[1])

        return merged