import heapq

class MedianFinder(object):

    def __init__(self):
        # Max-heap containing the smaller half
        self.small = []

        # Min-heap containing the larger half
        self.large = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """

        # Add to the smaller half
        heapq.heappush(self.small, -num)

        # Move the largest number from small to large
        heapq.heappush(self.large, -heapq.heappop(self.small))

        # Keep small equal in size or one element larger
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self):
        """
        :rtype: float
        """

        # Odd number of elements
        if len(self.small) > len(self.large):
            return float(-self.small[0])

        # Even number of elements
        return (-self.small[0] + self.large[0]) / 2.0