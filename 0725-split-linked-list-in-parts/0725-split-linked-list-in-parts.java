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
    public ListNode[] splitListToParts(ListNode head, int k) {
        ListNode[] result = new ListNode[k];
        
        // Find the length of the linked list
        int length = 0;
        ListNode current = head;
        while (current != null) {
            length++;
            current = current.next;
        }
        
        // Calculate the size of each part and the number of remaining nodes
        int partSize = length / k;
        int remaining = length % k;
        
        current = head;
        ListNode prev = null;
        
        for (int i = 0; i < k; i++) {
            result[i] = current;
            int currentPartSize = partSize + (i < remaining ? 1 : 0);
            
            for (int j = 0; j < currentPartSize; j++) {
                prev = current;
                current = current.next;
            }
            
            if (prev != null) {
                prev.next = null; // Cut off the current part from the rest of the list
            }
        }
        
        return result;
    }
}