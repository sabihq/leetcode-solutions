class Solution(object):
    def reverseBits(self, n):
        result = 0

        for _ in range(32):
            bit = n & 1                 # Get the rightmost bit
            result = (result << 1) | bit
            n >>= 1                    # Move to the next bit

        return result