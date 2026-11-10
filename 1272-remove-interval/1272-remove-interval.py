class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        result = []
        start, end = toBeRemoved

        for a, b in intervals:
            if b <= start or a >= end:
                result.append([a, b])
            else:
                if a < start:
                    result.append([a, start])
                if b > end:
                    result.append([end, b])

        return result
