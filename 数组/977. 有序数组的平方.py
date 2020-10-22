"""
给定一个按非递减顺序排序的整数数组 A，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。
https://leetcode-cn.com/problems/squares-of-a-sorted-array/
输入：[-4,-1,0,3,10]
输出：[0,1,9,16,100]
"""
lis = [-7,-3,2,3,11]
class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        B = []
        for i in range(len(A)):
            if B == []:
                B.append(pow(A[i], 2))
            else:
                for index, value in enumerate(B):
                    if pow(A[i], 2) < value:
                        B.insert(index, pow(A[i], 2))
                        break

        return B

res = Solution().sortedSquares(lis)
print(res)


class Solution(object):
    def sortedSquares(self, A):
        return sorted(x*x for x in A)

res = Solution().sortedSquares(lis)
print(res)

