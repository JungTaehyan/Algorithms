from sys import stdin
N = int(stdin.readline().strip())
list_1=[]
for i in range(N):
    list_1.append(list(stdin.readline().split()))
list_1.sort(key=lambda x:int(x[0]))
for j in range(N):
    print(list_1[j][0], list_1[j][1])