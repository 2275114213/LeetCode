"""
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/container-with-most-water
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


# 笨方法
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        if len(height) == 2:
            if height[0] < height[1]:
                max_area = height[0]
            else:
                max_area = height[1]
        else:
            max_area = 0
            while i < len(height):
                for j in range(i + 1, len(height)):
                    if height[i] < height[j]:
                        area = height[i] * (j - i)
                    else:
                        area = height[j] * (j - i)
                    max_area = max(max_area, area)
                    # print(max_area)
                i += 1
        return max_area


class Solution1:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        area = min(height[i], height[j]) * (j - i)
        while i < j:
            print(i, j)
            if height[i] < height[j]:
                while i < len(height) - 1 and height[i] < height[i + 1]:
                    i += 1
                area = max(area, min(height[i], height[j]) * (j - i - 1))
            else:
                while height[j - 1] > height[j]:
                    j -= 1
                area = max(area, min(height[i], height[j]) * (j - i + 1))

        return area


class Solution2:
    def maxArea(self, height: List[int]) -> int:
        i, j, area = 0, len(height) - 1, 0
        while i < j:
            area = max(area, min(height[i], height[j]) * (j - i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return area


height = [1,1]
res = Solution2().maxArea(height)
print(res)
