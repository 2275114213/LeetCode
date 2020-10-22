li = [5,1,1,2,0,0]
#     5
#  1     1
# 2 0   0

def shift(li, left, right):
    j = 2 * left + 1  # 初始指向左孩子
    while j < right:  # 当没有下任了跳出循环
        # 如果存在右节点且右节点大于左节点
        if j + 1 <= right and li[j] <= li[j + 1] and li[j + 1] > li[left]:
            li[j + 1], li[left] = li[left], li[j + 1]
            left = j + 1
            j = 2 * left + 1
        # 如果左节点大于父节点
        elif li[j] > li[left]:
            li[j], li[left] = li[left], li[j]
            left = j
            j = 2 * left + 1
        # 如果左节点小于父节点则跳出循环
        else:
            break


def heap_sort(li, left, right):
    # 构造堆
    for i in range(int(len(li) / 2) - 1, -1, -1):
        shift(li, i, len(li) - 1)

    # 对堆排序
    for right in range(len(li) - 1, -1, -1):
        li[0], li[right] = li[right], li[0]
        shift(li, 0, right - 1)


heap_sort(li, 0, 10)
print(li)
















