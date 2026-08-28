class Solution(object):
    def findPeakElement(self, nums):
        left = 0
        right = len(nums) - 1

        while left < right:
            middle = (left + right) // 2

            if nums[middle] < nums[middle + 1]:
                # We are moving uphill, so a peak is on the right
                left = middle + 1
            else:
                # We are moving downhill, so middle or the left side has a peak
                right = middle

        return left