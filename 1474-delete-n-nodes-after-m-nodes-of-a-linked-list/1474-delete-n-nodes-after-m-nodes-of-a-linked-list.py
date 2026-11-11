class Solution:
    def deleteNodes(self, head: ListNode | None, m: int, n: int) -> ListNode | None:
        current = head

        while current:
            for i in range(m - 1):
                if not current.next:
                    return head
                current = current.next

            temp = current.next

            for i in range(n):
                if not temp:
                    break
                temp = temp.next

            current.next = temp
            current = temp

        return head
