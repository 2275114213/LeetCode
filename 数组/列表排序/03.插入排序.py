def insert_sort(lis):
    for i in range(len(lis)):
        tmp = lis[i]
        j = i - 1
        while j >= 0 and lis[j] > tmp:
            lis[j + 1] = lis[j]
            j = j - 1
        lis[j+1] = tmp
lis = ['5',"6","4",'9',"3","2","7"]
insert_sort(lis)
print(lis)


