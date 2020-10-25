"""
示例1:

输入: [1,4], 2
输出: 4
原因: 第 1 秒初，提莫开始对艾希进行攻击并使其立即中毒。中毒状态会维持 2 秒钟，直到第 2 秒末结束。
第 4 秒初，提莫再次攻击艾希，使得艾希获得另外 2 秒中毒时间。
所以最终输出 4 秒。

示例2:

输入: [1,2], 2
输出: 3
原因: 第1秒初，提莫开始对艾希进行攻击并使其立即中毒。中毒状态会维持 2 秒钟，直到第 2 秒末结束。
但是第 2 秒初，提莫再次攻击了已经处于中毒状态的艾希。
由于中毒状态不可叠加，提莫在第 2 秒初的这次攻击会在第3秒末结束。
所以最终输出 3 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/teemo-attacking
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int  持续时间
        :rtype: int
        """
        time_sum = 0
        if len(timeSeries) == 0:
            return time_sum
        for i in range(len(timeSeries) - 1):
            time_sum += min(timeSeries[i + 1] - timeSeries[i], duration)
        return time_sum + duration


res = Solution().findPoisonedDuration([1, 2], 2)
print(res)
