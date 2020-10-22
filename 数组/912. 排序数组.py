"""
https://leetcode-cn.com/problems/sort-an-array/
给你一个整数数组 nums，请你将该数组升序排列。
"""
nums = [5, 1, 1, 2, 0, 0]


def quick_sort(lis, left, right):
    if left < right:
        mid = partition(lis, left, right)
        quick_sort(lis, left, mid - 1)
        quick_sort(lis, mid + 1, right)


def partition(lis, left, right):
    tmp = lis[left]
    while left < right:
        while left < right and lis[right] >= tmp:
            right -= 1
        lis[left] = lis[right]
        while left < right and lis[left] <= tmp:
            left += 1
        lis[right] = lis[left]
    lis[left] = tmp
    return left


quick_sort(nums, 0, len(nums) - 1)
print(nums)
