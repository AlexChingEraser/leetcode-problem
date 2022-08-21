// Given the head of a singly linked list, reverse the list, and return the reversed list.

import LinkedList from './base_structure/linkedList.js'

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
function reverseList(head) {
    // stay in position algorithm
    if (!head || !head.next) return head
    let prev = head;
    let cur = head.next;
    prev.next = null

    while (cur) {
        let next = cur.next
        cur.next = prev
        prev = cur
        cur = next

    }
    return prev
};

let linkedlist = new LinkedList();
linkedlist.append(1).append(2).append(3).append(4).append(5)
let example = linkedlist.head
let afterReverse = reverseList(example)
let result = LinkedList.toArray(afterReverse).map(item => item.toString()).toString()
console.log(result)
