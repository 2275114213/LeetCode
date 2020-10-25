"""
给出 N 名运动员的成绩，找出他们的相对名次并授予前三名对应的奖牌。前三名运动员将会被分别授予 “金牌”，“银牌” 和“ 铜牌”（"Gold Medal", "Silver Medal", "Bronze Medal"）。

(注：分数越高的选手，排名越靠前。)

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/relative-ranksƒ
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        max_num = max(nums)
        nums_index = [-1 for i in range(max_num + 1)]
        for i in range(len(nums)):
            # 把数组的对应元素位置换成原来的下表
            nums_index[nums[i]] = i
        j = 0
        rank = 1
        while max_num >= 0:
            if nums_index[max_num] >= 0:
                if rank == 1:
                    nums[nums_index[max_num]] = "Gold Medal"
                elif rank == 2:
                    nums[nums_index[max_num]] = "Silver Medal"
                elif rank == 3:
                    nums[nums_index[max_num]] = "Bronze Medal"
                else:
                    nums[nums_index[max_num]] = f"{rank}"
                rank += 1
            max_num -= 1
        return nums


nums = [5, 4, 3, 2, 1]
res = Solution().findRelativeRanks(nums)
print(res)
