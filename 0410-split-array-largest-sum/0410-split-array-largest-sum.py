from typing import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left, right = max(nums), sum(nums)

        while left < right:
            mid = (left + right) // 2

            parts = 1
            current_sum = 0

            for num in nums:
                if current_sum + num > mid:
                    parts += 1
                    current_sum = num
                else:
                    current_sum += num

            if parts <= k:
                right = mid
            else:
                left = mid + 1

        return left