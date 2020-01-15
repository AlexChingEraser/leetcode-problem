# 给你一个以行程长度编码压缩的整数列表nums 。
# 考虑每相邻两个元素[a, b] = [nums[2 * i], nums[2 * i + 1]] （其中i >= 0 ），每一对都表示解压后有a个值为b的元素。
# 请你返回解压后的列表。

# 示例：
# 输入：nums = [1, 2, 3, 4]
# 输出：[2, 4, 4, 4]
#
# 提示：
# 2 <= nums.length <= 100
# nums.length % 2 == 0
# 1 <= nums[i] <= 100

# class Solution:
#     def decompressRLElist(self, nums: List[int]) -> List[int]:


class Solution:
    def decompressRLElist(self, nums):
        lst = []
        length = len(nums)
        if length % 2:
            return "Encode Error!"
        for index in range(0, length, 2):
            temp = [nums[index + 1]] * nums[index]
            lst.extend(temp)

        return lst

    def decompressRLElist(self, nums):
        return sum(([b] * a for a, b in zip(nums[::2], nums[1::2])), [])



if __name__ == '__main__':
    a = [1, 2, 3, 4]
    s = Solution()
    print(s.decompressRLElist(a))
