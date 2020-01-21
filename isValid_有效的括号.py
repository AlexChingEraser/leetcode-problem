# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
#
# 有效字符串需满足：
#
#
# 	左括号必须用相同类型的右括号闭合。
# 	左括号必须以正确的顺序闭合。
#
#
# 注意空字符串可被认为是有效字符串。
#
# 示例 1:
#
# 输入: "()"
# 输出: true
#
#
# 示例 2:
#
# 输入: "()[]{}"
# 输出: true
#
#
# 示例 3:
#
# 输入: "(]"
# 输出: false
#
#
# 示例 4:
#
# 输入: "([)]"
# 输出: false
#
#
# 示例 5:
#
# 输入: "{[]}"
# 输出: true

# class Solution:
#     def isValid(self, s: str) -> bool:

# 有点类似判断回文字符串

class Solution:
    def isValid(self, s: str) -> bool:
        # bracket = {'(': ')', '{': '}', '[': ']'}
        d = {")": "(", "]": "[", "}": "{"}
        l = []
        for i in s:
            if d.get(i) is None:
                l.append(i)
            elif len(l) == 0 or d.get(i) != l[-1]:
                return False
            elif d.get(i) == l[-1]:
                l.pop()
        if len(l) == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    print(s.isValid("([)]"))
