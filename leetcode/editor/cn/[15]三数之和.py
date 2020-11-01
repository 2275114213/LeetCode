# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复
# 的三元组。 
# 
#  注意：答案中不可以包含重复的三元组。 
# 
#  
# 
#  示例： 
# 
#  给定数组 nums = [-1, 0, 1, 2, -1, -4]，
# 
# 满足要求的三元组集合为：
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
#  
#  Related Topics 数组 双指针 
#  👍 2715 👎 0
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        lis = []
        nums.sort()
        for index, item in enumerate(nums[:-2]):
            j = index + 1
            k = len(nums) - 1
            if item > 0:
                break
            if index > 0 and item == nums[index - 1]:
                continue
            while j < k:
                if nums[j] + nums[k] < -item:
                    j += 1
                elif nums[j] + nums[k] > -item:
                    k -= 1
                else:
                    lis.append([nums[j], nums[k], item])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

        return lis

# leetcode submit region end(Prohibit modification and deletion)
