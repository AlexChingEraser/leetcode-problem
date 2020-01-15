# 给你一棵二叉树，请你返回满足以下条件的所有节点的值之和：
#
#
# 该节点的祖父节点的值为偶数。（一个节点的祖父节点是指该节点的父节点的父节点。）如果不存在祖父节点值为偶数的节点，那么返回 0 。
# 输入：root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
# 输出：18
# 解释：图中红色节点的祖父节点的值为偶数，蓝色节点为这些红色节点的祖父节点。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def grand(self, node: TreeNode) -> int:
        grand_l = node.left
        grand_r = node.right
        grand_sum = 0

        if grand_l:
            if grand_l.left:
                grand_sum += grand_l.left.val
            if grand_l.right:
                grand_sum += grand_l.right.val
        if grand_r:
            if grand_r.left:
                grand_sum += grand_r.left.val
            if grand_r.right:
                grand_sum += grand_r.right.val

        return grand_sum

    def sumEvenGrandparent(self, root: TreeNode) -> int:
        # level traversal
        from queue import Queue
        que = Queue()
        cur = root
        que.put(cur)
        value = 0
        while not que.empty():
            node = que.get()
            if not node.val % 2:
                value += self.grand(node)
            if node.left != None:
                que.put(node.left)
            if node.right != None:
                que.put(node.right)

        return value




if __name__ == '__main__':
    s = Solution()
    root = TreeNode(6)
    node1 = TreeNode(7)
    node2 = TreeNode(8)
    node3 = TreeNode(2)
    node4 = TreeNode(7)
    node5 = TreeNode(1)
    node6 = TreeNode(3)
    node7 = TreeNode(9)
    node8 = TreeNode(1)
    node9 = TreeNode(4)
    node10 = TreeNode(5)
    root.left = node1
    root.right = node2
    root.left.left = node3
    root.left.right = node4
    root.right.left = node5
    root.right.right = node6
    root.left.left.left = node7
    root.left.right.left = node8
    root.left.right.right = node9
    root.right.right.right = node10

    print(s.sumEvenGrandparent(root))