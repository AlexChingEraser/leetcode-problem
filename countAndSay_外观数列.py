# 「外观数列」是一个整数序列，从数字1开始，序列中的每一项都是对前一项的描述。前五项如下：
#
# 1.1
# 2.11
# 3.21
# 4.1211
# 5.111221
#
# 1被读作"one 1"("一个一"), 即11。
# 11被读作"two 1s"("两个一"）, 即21。
# 21被读作"one 2", "one 1" （"一个二", "一个一"), 即1211。
#
# 给定一个正整数
# n（1 ≤ n ≤ 30），输出外观数列的第n项。
# 注意：整数序列中的每一项将表示为一个字符串。
#
#
#
# 示例
# 1:
#
# 输入: 1
# 输出: "1"
# 解释：这是一个基本样例。
#
# 示例
# 2:
#
# 输入: 4
# 输出: "1211"
# 解释：当n = 3时，序列是"21"，其中我们有"2"和"1"两组，"2"可以读作"12"，也就是出现频次 = 1而值 = 2；
# 类似"1"可以读作"11"。所以答案是"12"和"11"组合在一起，也就是"1211"。

# class Solution:
#     def countAndSay(self, n: int) -> str:

class Solution:
    # 48ms 13.1MB
    # def translate(self, nums: str) -> str:
    #     des = ''
    #     index = 0
    #     if len(nums) == 1:
    #         return '1' + nums[0]
    #     while index < len(nums):
    #         same = True
    #         count = 0
    #         while same:
    #             val = nums[index]
    #             count += 1
    #             index += 1
    #             if index == len(nums):
    #                 break
    #             else:
    #                 if not nums[index] == val:
    #                     same = False
    #         des += str(count)
    #         des += str(val)
    #     return des

    # 52ms 13.1MB
    def translate(self, temp: str) -> str:
        count = 1
        i = 0
        sum = []
        while i + 1 < len(temp):
            if temp[i] == temp[i + 1]:
                count += 1
            if temp[i] != temp[i + 1]:
                sum.append(str(count))
                sum.append(temp[i])
                count = 1
            i += 1
        sum.append(str(count))
        sum.append(temp[-1])

        return "".join(sum) # 很有灵性



    def countAndSay(self, n: int) -> str:
        index = 1
        palindrome = "1"
        while index < n:
            palindrome = self.translate(palindrome)
            index += 1

        return palindrome

if __name__ == '__main__':
    s = Solution()
    for i in range(1, 20):
        print(s.countAndSay(i))
    # print(s.countAndSay(5))
