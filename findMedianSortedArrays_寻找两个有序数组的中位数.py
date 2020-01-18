# 给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
#
# 请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
#
# 你可以假设 nums1 和 nums2 不会同时为空。
#
# 示例 1:
#
# nums1 = [1, 3]
# nums2 = [2]
#
# 则中位数是 2.0
# 示例 2:
#
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# 则中位数是 (2 + 3)/2 = 2.5

# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:


class Solution:
    def findMedianSortedArrays_alex(self, nums1, nums2) -> float:
        sum_num = nums1 + nums2
        sum_num.sort()
        length = len(sum_num)

        if not length % 2:
            return (sum_num[length // 2 - 1] + sum_num[length // 2]) / 2
        else:
            return sum_num[len(sum_num) // 2]

    def get_kth(self, nums1, nums2, k):
        # print(nums1, nums2, 'k=', k)
        m, n = len(nums1), len(nums2)
        if m == 0: return nums2[k - 1]
        if n == 0: return nums1[k - 1]
        if k == 1: return min(nums1[0], nums2[0])
        drop1, drop2 = min(k // 2, m), min(k // 2, n)  # 丢弃个数
        # print('m={},n={},k/2={},drop1={},drop2={}'.format(m,n,k//2,drop1,drop2))
        if nums1[drop1 - 1] <= nums2[drop2 - 1]:  # 丢弃nums1部分
            return self.get_kth(nums1[drop1:m], nums2, k - drop1)
        else:
            return self.get_kth(nums1, nums2[drop2:n], k - drop2)

    def findMedianSortedArrays(self, nums1, nums2) -> float:
        m, n = len(nums1), len(nums2)
        # 整合奇偶数情况
        mid_left = self.get_kth(nums1, nums2, (m + n + 1) // 2)
        mid_right = self.get_kth(nums1, nums2, (m + n + 2) // 2)
        return (mid_left + mid_right) / 2


if __name__ == '__main__':
    import random
    import time
    from test_function_time_计算运行时间并返回函数值 import countTime

    random.randint(0, 10000)
    nums1 = [random.randint(0, 10000) for _ in range(1000000)]
    nums2 = [random.randint(0, 10000) for _ in range(99999)]
    s = Solution()
    print(countTime(s.findMedianSortedArrays, nums1, nums2))
    print(countTime(s.findMedianSortedArrays_alex, nums1, nums2))
