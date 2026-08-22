class Solution(object):
    def reverseBetween(self, head, left, right):
        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        before = dummy

        # Move `before` to the node immediately before `left`
        for _ in range(left - 1):
            before = before.next

        current = before.next

        # Move each following node to the front of the section
        for _ in range(right - left):
            move = current.next
            current.next = move.next
            move.next = before.next
            before.next = move

        return dummy.next