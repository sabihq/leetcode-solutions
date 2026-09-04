class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        shifts = 0

        while left < right:
            left >>= 1
            right >>= 1
            shifts += 1

        return left << shifts