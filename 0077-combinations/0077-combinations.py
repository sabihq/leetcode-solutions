class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []

        def backtrack(start, current):
            # We have selected exactly k numbers
            if len(current) == k:
                result.append(current[:])
                return

            for number in range(start, n + 1):
                current.append(number)
                backtrack(number + 1, current)
                current.pop()

        backtrack(1, [])
        return result