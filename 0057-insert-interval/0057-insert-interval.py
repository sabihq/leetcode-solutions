class Solution(object):
    def insert(self, intervals, newInterval):
        result = []
        i = 0

        # 1. Add intervals that come completely before newInterval
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # 2. Merge all intervals that overlap with newInterval
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        result.append(newInterval)

        # 3. Add the remaining intervals
        while i < len(intervals):
            result.append(intervals[i])
            i += 1

        return result