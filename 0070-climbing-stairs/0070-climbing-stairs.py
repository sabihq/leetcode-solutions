class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        first = 1
        second = 1

        for _ in range(n):
            first, second = second, first + second

        return first