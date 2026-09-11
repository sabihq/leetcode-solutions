class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        import heapq

        min_heap = []
        result = []

        # Start with nums2[0] paired with the first k values of nums1
        for i in range(min(k, len(nums1))):
            heapq.heappush(
                min_heap,
                (nums1[i] + nums2[0], i, 0)
            )

        while min_heap and len(result) < k:
            pair_sum, i, j = heapq.heappop(min_heap)

            result.append([nums1[i], nums2[j]])

            # Add the next pair using the same nums1 value
            if j + 1 < len(nums2):
                heapq.heappush(
                    min_heap,
                    (nums1[i] + nums2[j + 1], i, j + 1)
                )

        return result