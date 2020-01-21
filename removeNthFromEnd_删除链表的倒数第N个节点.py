# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
#
# 示例：
#
# 给定一个链表: 1->2->3->4->5, 和 n = 2.
#
# 当删除了倒数第二个节点后，链表变为 1->2->3->5.
#
#
# 说明：
#
# 给定的 n 保证是有效的。
#
# 进阶：
#
# 你能尝试使用一趟扫描实现吗？

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 缺点：维护了4个指针变量，很难统一;des可以去掉
    # 52ms 13.1MB
    #反映出对多情况处理稍显稚嫩
    # def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    #     pre, cur, end = head, head, head
    #     des = head
    #     while n > 0:
    #         end = end.next
    #         n -= 1
    #     if end == None:
    #         des = des.next
    #     while end != None:
    #         pre = cur
    #         cur = cur.next
    #         end = end.next
    #
    #     pre.next = cur.next
    #
    #     return des

    # 使用快慢指针，先让快指正走n步，然后快慢指针一起走;
    # 当快指针走到最后一个节点时，慢指针指向的下一个节点就是倒数第n个节点，则将慢指针指向下下个节点，完成删除操作。
    # 44ms 13MB
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head == None:
            return None
        if head.next == None and n == 1:
            return None
        cur, end = head, head
        while n > 0:
            end = end.next
            n -= 1
        if end == None:
            return head.next
        while end.next != None:
            cur = cur.next
            end = end.next

        cur.next = cur.next.next

        return head


if __name__ == '__main__':
    def printNode(node):
        while node != None:
            print(node.val)
            node = node.next
        print('-' * 20)


    n1 = ListNode(1)
    # n2 = ListNode(2)
    # n3 = ListNode(4)
    # n4 = ListNode(1)
    # n5 = ListNode(3)
    # n6 = ListNode(5)
    # n1.next = n2
    # n2.next = n3
    # n3.next = n4
    # n4.next = n5
    # n5.next = n6

    printNode(n1)

    s = Solution()
    node = s.removeNthFromEnd(n1, 1)
    printNode(node)
