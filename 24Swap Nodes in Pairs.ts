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

/*function swapPairs(head: ListNode | null): ListNode | null {
    let before_index = head;
    let index = head;
    let temp = head;

    if(head === null || head.next === null) {
        return head;
    }
    temp = index.next.next;
    index.next.next = index;
    head = index.next;
    before_index = index;
    index = temp;
    
    while (index) {
        if(index.next) {
            temp = index.next?.next || null;
            index.next.next = index;
            before_index.next = index.next;
            before_index = index;
            index = temp;
        }
        break;
    }   
    before_index.next = index;
    return head;
};
*/
/*function swapPairs(head: ListNode | null): ListNode | null {
    let left_index = head;
    let right_index = head;

    if (left_index === null || left_index.next === null) {
        return head;
    }

    right_index = right_index.next;
    
    let oddHead: ListNode | null = null;
    let evenHead: ListNode | null = null;
    let oddCurrent: ListNode | null = null;
    let evenCurrent: ListNode | null = null;
    let isOdd = true; // 用于跟踪当前节点的奇偶性

    let current: ListNode | null = head;

    while (current !== null) {
        if (isOdd) {
            // 奇数节点
            if (oddHead === null) {
                oddHead = current;
                oddCurrent = current;
            } else {
                oddCurrent!.next = current;
                oddCurrent = oddCurrent!.next;
            }
        } else {
            // 偶数节点
            if (evenHead === null) {
                evenHead = current;
                evenCurrent = current;
            } else {
                evenCurrent!.next = current;
                evenCurrent = evenCurrent!.next;
            }
        }
        current = current.next;
        isOdd = !isOdd; // 切换奇偶性
    }
    if (oddCurrent !== null) {
        oddCurrent.next = null;
    }
    if (evenCurrent !== null) {
        evenCurrent.next = null;
    }

    let left_head = oddHead;
    let right_head = evenHead;

    let final_head = right_head;
    let temp = left_head;
    let flag = 1;

    while (right_head && left_head) {
        if(flag == 1 ){
            temp = right_head.next;
            right_head.next = left_head;
            right_head = temp;
        }
        else{
            temp = left_head.next;
            left_head.next = right_head;
            left_head = temp;
        }
        flag = flag * (-1);
    }
    return final_head;
};
*/