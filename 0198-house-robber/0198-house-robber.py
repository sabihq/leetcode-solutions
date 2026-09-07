class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        previous = 0
        current = 0

        for money in nums:
            previous, current = current, max(current, previous + money)

        return current