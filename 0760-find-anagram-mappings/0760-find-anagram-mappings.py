from collections import defaultdict
from typing import List


class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        indices = defaultdict(list)

        for i, value in enumerate(nums2):
            indices[value].append(i)

        return [indices[value].pop() for value in nums1]