class Solution(object):
    def trailingZeroes(self, n):
        zeroes = 0

        while n >= 5:
            n //= 5
            zeroes += n

        return zeroes