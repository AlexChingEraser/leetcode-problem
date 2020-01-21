# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkList:
    @staticmethod
    def construct(nums: list) -> ListNode:
        first = ListNode(0)
        cur = first
        for i in nums:
            cur.next = ListNode(i)
            cur = cur.next

        return first.next

def printNode(node):
    while node != None:
        print(node.val)
        node = node.next
    print('-' * 20)

if __name__ == '__main__':
    lst = LinkList.construct([1, 1, 1, 3, 5, 7, 9])
    printNode(lst)

