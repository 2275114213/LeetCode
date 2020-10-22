def quick_sort(li, left, right):
    if left < right:
        mid = partition(li, left, right)
        quick_sort(li, left, mid - 1)
        quick_sort(li, mid + 1, right)


def partition(li, left, right):
    initial = li[left]
    while left < right:
        while left < right and initial <= li[right]:
            right -= 1
        li[left] = li[right]
        while left < right and initial >= li[left]:
            left += 1
        li[right] = li[left]
    li[left] = initial
    return left


lis = [6, 3, 5, 1, 7, 8, 2, 9, 34, 232]
quick_sort(lis, 0, 9)
print(lis)
