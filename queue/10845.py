from sys import stdin
from collections import deque
N = int(stdin.readline())
i = 0
list_1 = deque([])
while i < N:
    order = stdin.readline().split()
    if order[0] == 'push':
        list_1.append(order[1])
    if order[0] == 'pop':
        if len(list_1) > 0:
            print(list_1[0])
            list_1.popleft()
        else:
            print(-1)
    if order[0] == 'size':
        print(len(list_1))
    if order[0]=='empty':
        if len(list_1)>0:
            print(0)
        else:
            print(1)
    if order[0]=='front':
        if len(list_1)>0:
            print(list_1[0])
        else:
            print(-1)
    if order[0] == 'back':
        if len(list_1)>0:
            print(list_1[len(list_1)-1])
        else:
            print(-1)
    i+=1