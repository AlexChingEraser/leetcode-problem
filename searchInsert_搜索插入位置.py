# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
# 
# 你可以假设数组中无重复元素。
# 
# 示例 1:
# 
# 输入: [1,3,5,6], 5
# 输出: 2
# 
# 
# 示例 2:
# 
# 输入: [1,3,5,6], 2
# 输出: 1
# 
# 
# 示例 3:
# 
# 输入: [1,3,5,6], 7
# 输出: 4
# 
# 
# 示例 4:
# 
# 输入: [1,3,5,6], 0
# 输出: 0

# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
from lib2to3 import main


class Solution:
    # insert sort AND binary serach sort
    def searchInsert(self, nums: list, target: int) -> int:
        # binary search sort
        # length = len(nums)
        # index = len(nums) // 2
        # while length > 1:
        #     if nums[length // 2] > target:
        #         nums = nums[:length // 2]
        #         length = len(nums)
        #         index -= length
        #     elif nums[length // 2] < target:
        #         nums = nums[length // 2:]
        #         length = len(nums)
        #         index += length
        #     elif nums[length // 2] == target:
        #         return index + length // 2
        # return 0

        # 此处参考某java版本，提交24ms/13.5MB
        if target > nums[len(nums) - 1]:
            return len(nums)
        low, high = 0, len(nums)
        while low < high:
            middle = (low + high) // 2  # // 向下取整
            middleVal = nums[middle]
            if target > middleVal:
                low = middle + 1
            elif target < middleVal:
                high = middle
            elif target == middleVal:
                return middle
        # low == high OR low > hign
        return low


if __name__ == '__main__':
    nums = [1,3,5,6]
    s = Solution()
    print(s.searchInsert(nums, 5))
