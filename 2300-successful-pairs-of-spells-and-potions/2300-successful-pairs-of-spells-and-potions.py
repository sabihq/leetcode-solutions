from typing import List

class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        potions.sort()
        m = len(potions)
        pairs = []

        for spell in spells:
            left, right = 0, m

            while left < right:
                mid = (left + right) // 2

                if spell * potions[mid] >= success:
                    right = mid
                else:
                    left = mid + 1

            pairs.append(m - left)

        return pairs