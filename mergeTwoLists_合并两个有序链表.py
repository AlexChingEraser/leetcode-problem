# 将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
#
# 示例：
#
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 36ms 13.1MB
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        des = ListNode(0)
        cur = des
        # traversal l1 and l2
        while l1 != None and l2 != None:
            if l1.val >= l2.val:
                cur.next = l2
                cur = cur.next
                l2 = l2.next
            elif l1.val < l2.val:
                cur.next = l1
                cur = cur.next
                l1 = l1.next

        if l1 == None:
            cur.next = l2
        else:
            cur.next = l1

        return des.next


if __name__ == '__main__':
    def printNode(node):
        while node != None:
            print(node.val)
            node = node.next
        print('-' * 20)


    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(4)
    n1.next = n2
    n2.next = n3
    printNode(n1)

    n4 = ListNode(1)
    n5 = ListNode(3)
    n6 = ListNode(5)
    n4.next = n5
    n5.next = n6
    printNode(n4)

    s = Solution()
    node = s.mergeTwoLists(n1, n4)
    printNode(node)
