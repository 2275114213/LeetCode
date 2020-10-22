def func3(x):
    if x > 0:
        print(x)
        func3(x-1)
func3(3)  # 3 2 1


def fun4(x):
    if x>0:
        fun4(x-1)
        print(x)
fun4(3)
