"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
"""
import copy
from typing import List


# 方法1
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[j] = nums[i]
                j += 1
        for i in range(j, len(nums)):
            nums[i] = 0


nums = [2, 1]


# Solution().moveZeroes(nums)
# print(nums)

# 方法2  快排
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for index, num in enumerate(nums):
            if num:
                if index > j:
                    nums[j] = nums[index]
                    nums[index] = 0
                j += 1


nums = [0, 1, 0, 3, 12]
Solution().moveZeroes(nums)
print(nums)
