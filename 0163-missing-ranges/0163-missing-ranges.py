from typing import List

class Solution:
    def findMissingRanges(
        self, nums: List[int], lower: int, upper: int
    ) -> List[List[int]]:
        result = []
        start = lower

        for num in nums:
            if start < num:
                result.append([start, num - 1])
            start = num + 1

        if start <= upper:
            result.append([start, upper])

        return result