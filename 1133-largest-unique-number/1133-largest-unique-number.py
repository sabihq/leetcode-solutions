from typing import List
from collections import Counter

class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        counts = Counter(nums)

        return max(
            (num for num, count in counts.items() if count == 1),
            default=-1
        )