# https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof/
# 递归
class Solution(object):
    def Fibonacci_Recursion_tool(self, n):
        if n <= 0:
            return 1
        elif n == 1:
            return 1
        else:
            return self.Fibonacci_Recursion_tool(n - 1) + self.Fibonacci_Recursion_tool(n - 2)


# res = Solution().Fibonacci_Recursion_tool(37)
# print(res)


def func(n):
    if n == 0:
        return 0
    else:
        return n + func(n - 1)


res = func(5)
print(res)


def func1(n):
    sum = 0
    for i in range(1, n + 1):
        sum = sum + i
