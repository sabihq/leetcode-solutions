class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right = 1, max(nums)

        while left < right:
            mid = (left + right) // 2

            total = sum((num + mid - 1) // mid for num in nums)

            if total <= threshold:
                right = mid
            else:
                left = mid + 1

        return left