from sys import stdin
N = int(stdin.readline())
list_1 = []
i = 0
while i < N:
    order = list(stdin.readline().split())

    if order[0] == 'push':
        list_1.append(order[1])
    if order[0] == 'pop':
        if len(list_1) >= 1:
            print(list_1[len(list_1)-1])
            list_1.pop()
        else:
            print(-1)
    if order[0] == 'size':
        print(len(list_1))
    if order[0] == 'empty':
        if len(list_1) == 0:
            print(1)
        else:
            print(0)
    if order[0] == 'top':
        if len(list_1) > 0:
            print(list_1[len(list_1)-1])
        else:
            print(-1)
    i+=1