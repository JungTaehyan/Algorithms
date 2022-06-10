from sys import stdin
N = int(stdin.readline())
num = 0
list_1 = []
while num < N:
    x, y = map(int, stdin.readline().split())
    list_1.append([x, y])
    num+=1
list_1.sort()
for k in list_1:
    print(k[0], k[1])
