class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
   }
}


function removeNthFromEnd(head: ListNode | null, n: number): ListNode | null {
    let slow_index = head;
    let fast_index = head;
    for (let i = 0;i < n;++i) {
        fast_index = fast_index?.next || null;
    }
    if (fast_index === null) {
        return head?.next || null;
    }
    while (fast_index.next !==   null) {
        slow_index = slow_index?.next || null;
        fast_index = fast_index?.next || null;
    }
    slow_index?.next || null = slow_index?.next.next || null;
    return head;
};