"""
给出 N 名运动员的成绩，找出他们的相对名次并授予前三名对应的奖牌。前三名运动员将会被分别授予 “金牌”，“银牌” 和“ 铜牌”（"Gold Medal", "Silver Medal", "Bronze Medal"）。

(注：分数越高的选手，排名越靠前。)

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/relative-ranks
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        max_num = max(nums)
        num_index = [-1 for i in range(max_num+1)]
        j = 0
        for i in range(len(nums) - j):
            max_pos = self.get_max(nums[i:])
            print(max_pos)
            num_index[nums[i]] = max_pos
        print(num_index)

    def get_max(self, li):
        max_pos = 0
        tmp = li[max_pos]
        for i in range(1, len(li)):
            if li[i] > tmp:
                max_pos = i
        return max_pos


nums = [5, 4, 3, 2, 1]
Solution().findRelativeRanks(nums)
