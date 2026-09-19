import heapq

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        min_heap = []

        # Add the first node of each nonempty list
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, i, node))

        dummy = ListNode(0)
        current = dummy

        while min_heap:
            value, list_index, node = heapq.heappop(min_heap)

            # Add the smallest node to the merged list
            current.next = node
            current = current.next

            # Add the next node from the same list
            if node.next:
                heapq.heappush(
                    min_heap,
                    (node.next.val, list_index, node.next)
                )

        return dummy.next