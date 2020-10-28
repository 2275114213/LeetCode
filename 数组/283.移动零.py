"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
"""
import copy
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for index, i in enumerate(nums):
            if i:
                if j < index:
                    nums[j] = nums[index]
                    nums[index] = 0
                j += 1


nums = [0, 1, 0, 3, 12]
Solution().moveZeroes(nums)
print(nums)
