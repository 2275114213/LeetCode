def move(n, a, b, c, A, B, C):
    if n == 1:
        C.append(A.pop())
        print(1, a, '-->', c)
        return
    else:
        move(n - 1, a, c, b, A, C, B)
        print(n, a, '-->', c)
        C.append(A.pop())
        move(n - 1, b, a, c, B, A, C)


t = [1, 2, 3]
c = []
move(len(t), 'A', 'B', 'C', t, [], c)
print(c)
