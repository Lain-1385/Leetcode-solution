/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function hasCycle(head: ListNode | null): boolean {
    let slow_index = head;
    let fast_index = head;
    while(fast_index && fast_index.next) {
        slow_index = slow_index.next;
        fast_index = fast_index.next.next;
        if (slow_index === fast_index) {
            return true;
        }
    }
    return false;
};
/*function hasCycle(head: ListNode | null): boolean {
    if(head == null || head.next == null) {
        return false;
    }
    let judge = new ListNode (1000000);
    let temp = head;

    while (head) {
        temp == head.next;
        if(temp = judge){
            return true;
        }
        head.next = judge;
        head = temp;
    }
    return false;
};
*/