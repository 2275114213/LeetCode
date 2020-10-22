def shell_sort(li):
    d = len(li) // 2
    while d > 0:
        insert_sort(li, d)
        d = d // 2
        insert_sort(li, d)


def insert_sort(li, d):
    for i in range(d, len(li) - 1):
        tmp = li[i]
        j = i - d
        while j >= 0 and li[j] > tmp:
            li[i] = li[j]
            j -= d
        li[j + d] = tmp


lis = [6, 3, 5, 1, 7, 8, 2, 9, 34, 232]
shell_sort(lis)
print(lis)
