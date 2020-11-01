"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。


"""


# 递归
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 1
        elif n <= 2:
            return n
        else:
            return self.climbStairs(n - 1) + self.climbStairs(n - 2)


# 循环


res = Solution1().climbStairs(3)
print(res)
