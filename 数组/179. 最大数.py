"""
给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。
https://leetcode-cn.com/problems/largest-number/
"""

nums = [3, 30, 34, 5, 9]


# 9534330
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        exchange = False
        for i in range(len(nums) - 1):
            for j in range(len(nums) - 1 - i):
                if int(str(nums[j]) + str(nums[j + 1])) < int(str(nums[j + 1]) + str(nums[j])):
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    exchange = True
            if not exchange:
                break
        num = "".join([str(i) for i in nums])
        if num[0] == 0:
            return 0
        else:
            return num


num = Solution().largestNumber(nums)
print(num)
nums = [3, 30, 34, 5, 9]

#
# class LargerNumKey(str):
#
#     def __lt__(self, y):
#         return self + y > y + self
#
#
# class Solution:
#     def largestNumber(self, nums):
#         #
#         largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
#         return '0' if largest_num[0] == '0' else largest_num
#
#
# Solution().largestNumber(nums)





