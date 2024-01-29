import sys

N,M = map(int, sys.stdin.readline().split())
Score = list(map(float, sys.stdin.readline().split()))
list1 = []
#Score.sort()
for i in range(M):
    list1.append(list(map(int, sys.stdin.readline().split())))

for j in range(M):
    sum = 0
    cnt = 0
    for k in range(list1[j][0]-1, list1[j][1]):
        sum += Score[k]
        cnt += 1
    result = round(sum/cnt, 2)
    print(f'{result:.2f}')