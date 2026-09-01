class Solution(object):
    def findMin(self, nums):
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                # Minimum must be to the right of mid
                left = mid + 1
            else:
                # Mid could be the minimum
                right = mid

        return nums[left]