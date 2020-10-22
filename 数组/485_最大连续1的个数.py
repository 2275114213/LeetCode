"""
输入: [1,1,0,1,1,1]
输出: 3
解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.
"""


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [str(i) for i in nums]
        nums_to_str = ",".join(nums)
        import re
        #  ^(1,{0,1}*)$  1,1,0,1,1,1
        res = re.finditer("((1,)+(1|1$))|^1$", nums_to_str)
        lenth_list = []
        for i in res:
            lenth_list.append(len(i.group().split(",")))
        if lenth_list:
            max_length = max(lenth_list)
        else:
            max_length = 0
        return max_length

    def guanfang(self, nums):
        max_nums = 0
        count = 0
        for i in nums:
            if i == 1:
                count +=1
                if count>max_nums:
                    max_nums = count
            else:
                count = 0

        return max_nums

dada = Solution().guanfang([3, 3, 3, 3, 1, 0, 1, 1, 1])
print(dada)
