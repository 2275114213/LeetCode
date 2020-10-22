lis = [i for i in range(1, 10000000)]


def func1(num):
    import time
    now = time.time()
    if num in lis:
        print(time.time() - now)


func1(765755)

lis2 = [0 for i in range(1, 10000001)]

def func2(num):
    import time
    now = time.time()
    for el in lis:
        lis2[el] = 1
    print(lis2[num]==1)
    print(time.time()-now)
func2(765755)

s = set(lis)
def func3(num):
    import time
    now = time.time()
    if num in s:
        print(num)
    print(time.time() - now)
func3(765755)
