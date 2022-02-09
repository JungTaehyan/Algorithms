import sys
N = int(sys.stdin.readline().strip())
n = int(1000**0.5)
list_1 = list(range(2, 1001))
search = list(map(int, sys.stdin.readline().split()))
cnt = 0
for i in range(2, n+1):
    for j in range(len(list_1)-1, 1, -1):
        if list_1[j] % i == 0 and list_1[j] > i:
            list_1.pop(j)
for i in range(N):
    if search[i] in list_1:
        cnt+=1
print(cnt)