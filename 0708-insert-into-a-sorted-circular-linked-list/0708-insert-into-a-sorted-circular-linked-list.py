class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        newNode = Node(insertVal)

        if not head:
            newNode.next = newNode
            return newNode

        current = head

        while True:
            nextNode = current.next

            if current.val <= insertVal <= nextNode.val:
                break

            if current.val > nextNode.val:
                if insertVal >= current.val or insertVal <= nextNode.val:
                    break

            current = current.next

            if current == head:
                break

        newNode.next = current.next
        current.next = newNode

        return head
