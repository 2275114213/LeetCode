"""
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，
写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-search
"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = int((left + right) / 2)
            if target <= nums[mid]:
                right = mid-1
            elif target >= nums[mid]:
                left = mid+1
            else:
                return mid
        else:
            return -1
