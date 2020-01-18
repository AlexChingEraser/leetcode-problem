# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
#
# 示例 1:
#
# 输入: 123
# 输出: 321
#  示例 2:
#
# 输入: -123
# 输出: -321
# 示例 3:
#
# 输入: 120
# 输出: 21
# 注意:
#
# 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

# class Solution:
#     def reverse(self, x: int) -> int:


class Solution:
    def reverse(self, x: int) -> int:
        x_str = str(x)
        if x_str[0] == '-':
            x_str_rev = x_str[1:][::-1]
            reverse_num = (-1) * int(x_str_rev)
        else:
            x_str_rev = x_str[::-1]
            reverse_num = int(x_str_rev)

        if (-1) * pow(2, 31) >= reverse_num  or reverse_num >= pow(2, 31) - 1:
            return 0
        else:
            return reverse_num

    def reverse_elegent(self, x: int) -> int:
        if x < 0:
            res = int(''.join(reversed(str(-x))))
            return -res if res < 2 ** 31 + 1 else 0
        else:
            res = int(''.join(reversed(str(x))))
            return res if res < 2 ** 31 else 0


# java 1ms: 的确是编译语言..
#    public int reverse(int x) {
#         long n = 0;
#         while(x != 0) {
#             n = n*10 + x%10;
#             x = x/10;
#         }
#         return (int)n==n? (int)n:0;
#     }

if __name__ == '__main__':
    s = Solution()
    print(s.reverse_elegent(-123))
