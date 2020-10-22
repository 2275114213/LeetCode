"""
给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。
你需要让组成和的完全平方数的个数最少。

输入: n = 13
输出: 2
解释: 13 = 4 + 9
"""

import math

math.sqrt(25)


class Solution(object):
    def numSquares(self, n, lis=[]):
        """s
        :type n: int
        :rtype: int
        """
        sqrt = math.sqrt(n)
        if sqrt == 0.0:
            length = len(lis)
            return length
        else:
            sum = n - pow(int(sqrt), 2)
            lis.append(sqrt)
            return self.numSquares(sum, lis=lis)


res = Solution().numSquares(12)
print(res)
