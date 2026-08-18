class Solution(object):
    def partition(self, head, x):
        before_head = ListNode(0)
        before = before_head

        after_head = ListNode(0)
        after = after_head

        current = head

        while current:
            if current.val < x:
                before.next = current
                before = before.next
            else:
                after.next = current
                after = after.next

            current = current.next

        # End the second list
        after.next = None

        # Connect the two lists
        before.next = after_head.next

        return before_head.next