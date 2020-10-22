lst = [11, 65, 9, 8]
# 升序
def bubble_sort(li):
    exchange = False
    for item in range(len(li)-1):  # 走n趟和n-1趟是
        for i in range(len(li)-item-1):
            if li[i] > li[i + 1]:
                li[i + 1], li[i] = li[i], li[i + 1]
                exchange = True
        if not exchange:
            break
bubble_sort(lst)
print(lst)
