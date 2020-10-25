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
        new_nums = []
        max_num = max(nums)
        nums_index = [-1 for i in range(max_num + 1)]
        for index, i in enumerate(nums):
            if i != 0:
                nums_index[i] = index
        for i in nums_index:
            if i != -1:
                new_nums.append(nums[i])
        for i in range(len(nums) - len(new_nums)):
            new_nums.append(0)


nums = [0, 1, 0, 3, 12]
print(nums)
