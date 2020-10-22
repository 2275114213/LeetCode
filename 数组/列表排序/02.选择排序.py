def select_sort(lis):
    for i in range(len(lis)-1):
        min_pos = i
        for j in range(i+1, len(lis)):
            if lis[j] < lis[min_pos]:
                min_pos = j
        lis[i], lis[min_pos] = lis[min_pos], lis[i]


lis = [1, 2, 4, 5, 3, 10, 7, 8]
select_sort(lis)
print(lis)
