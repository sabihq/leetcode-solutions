class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right + 1) // 2

            missing = nums[mid] - nums[0] - mid

            if missing < k:
                left = mid
            else:
                right = mid - 1

        return nums[0] + left + k