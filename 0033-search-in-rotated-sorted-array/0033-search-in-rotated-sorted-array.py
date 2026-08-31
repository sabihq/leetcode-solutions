class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            if nums[middle] == target:
                return middle

            # Left half is sorted
            if nums[left] <= nums[middle]:
                if nums[left] <= target < nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1

            # Right half is sorted
            else:
                if nums[middle] < target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1

        return -1