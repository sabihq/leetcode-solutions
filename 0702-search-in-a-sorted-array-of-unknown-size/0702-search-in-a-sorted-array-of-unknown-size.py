class Solution(object):
    def search(self, reader, target):
        left, right = 0, 1

        # Expand the range until it can contain the target.
        while reader.get(right) < target:
            left = right + 1
            right *= 2

        # Binary search within that range.
        while left <= right:
            mid = (left + right) // 2
            value = reader.get(mid)

            if value == target:
                return mid
            elif value < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1