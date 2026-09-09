class Solution(object):
    def maxSubarraySumCircular(self, nums):
        total_sum = 0

        current_max = 0
        maximum_sum = nums[0]

        current_min = 0
        minimum_sum = nums[0]

        for num in nums:
            total_sum += num

            # Maximum normal subarray
            current_max = max(num, current_max + num)
            maximum_sum = max(maximum_sum, current_max)

            # Minimum subarray
            current_min = min(num, current_min + num)
            minimum_sum = min(minimum_sum, current_min)

        # If every number is negative, total_sum - minimum_sum
        # would incorrectly produce 0 for an empty subarray.
        if maximum_sum < 0:
            return maximum_sum

        circular_sum = total_sum - minimum_sum

        return max(maximum_sum, circular_sum)