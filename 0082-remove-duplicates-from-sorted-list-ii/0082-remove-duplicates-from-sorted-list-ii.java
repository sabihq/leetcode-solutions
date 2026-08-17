/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        // Dummy node handles cases where duplicates start at the head
        ListNode dummy = new ListNode(0, head);
        ListNode prev = dummy;

        while (head != null) {
            // Check if current value has duplicates
            if (head.next != null && head.val == head.next.val) {
                int duplicateValue = head.val;

                // Skip every node with this duplicate value
                while (head != null && head.val == duplicateValue) {
                    head = head.next;
                }

                prev.next = head;
            } else {
                // Current node is unique
                prev = head;
                head = head.next;
            }
        }

        return dummy.next;
    }
}