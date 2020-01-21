# 给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
#
# 示例 1:
#
# 输入: 1->1->2
# 输出: 1->2
#
#
# 示例 2:
#
# 输入: 1->1->2->3->3
# 输出: 1->2->3

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def deleteDuplicates(self, head: ListNode) -> ListNode:

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 56ms 12.9MB
    # def deleteDuplicates(self, head: ListNode) -> ListNode:
    #     if head == None:
    #         return None
    #     cur = head
    #     while cur.next != None:
    #         if cur.val != cur.next.val:
    #             cur = cur.next
    #         else:
    #             pre = cur.next
    #             while pre.next != None:
    #                 if pre.val == pre.next.val:
    #                     pre = pre.next
    #                 else:
    #                     break
    #             else:
    #                 cur.next = None
    #             cur.next = pre.next
    #     return head

    # 60ms 13.3MB
    def deleteDuplicates(self, ans: ListNode) -> ListNode:
        head = ans
        while head != None:
            if head.next != None and head.next.val == head.val:
                head.next = head.next.next
            else:
                head = head.next
        return ans


if __name__ == '__main__':
    from base_linklist import LinkList, printNode

    lst = LinkList.construct([2, 2, 3, 4, 4, 5, 7, 8, 9, 11, 11, 13])
    s = Solution()
    printNode(lst)
    printNode(s.deleteDuplicates(lst))
