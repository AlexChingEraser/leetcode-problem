# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
#
# 示例 1：
#
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
# 示例 2：
#
# 输入: "cbbd"
# 输出: "bb"

# "回文串”是一个正读和反读都一样的字符串，比如“level”或者“noon”等等就是回文串

# class Solution:
#     def longestPalindrome(self, s: str) -> str:

class Solution:
    # 动态规划算法
    def longestPalindrome(self, s):
        str_length = len(s)
        max_length = 0  # 维护的是什么信息?从字面行理解是最长长度
        start = 0
        for i in range(str_length):
            if i - max_length >= 1 and s[i - max_length - 1:i + 2] == s[i - max_length - 1:i + 2][::-1]:
                start = i - max_length - 1
                max_length += 2
                continue
            if i - max_length >= 0 and s[i - max_length:i + 2] == s[i - max_length:i + 2][::-1]:
                start = i - max_length
                max_length += 1
        return s[start:start + max_length + 1]


if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome("abcdcbgh"))
