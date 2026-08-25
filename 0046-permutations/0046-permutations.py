class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []

        def backtrack(current):
            # A complete permutation contains every number
            if len(current) == len(nums):
                result.append(current[:])
                return

            for number in nums:
                if number not in current:
                    current.append(number)
                    backtrack(current)
                    current.pop()

        backtrack([])
        return result