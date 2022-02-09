from sys import stdin
K, N = map(int,stdin.readline().split())
line = []
for i in range(K):
    a = int(stdin.readline())
    line.append(a)
start = 1 # index를 찾는게 아니라 값을 찾는거임!! 그래서 start = 1
end = max(line)
while start <= end:
    mid = (start+end)//2
    cnt = 0 # binarySearch로 찾은 값의 갯수를 구하기 위함
    for j in line:
        cnt += j//mid
    if cnt >= N:
        start = mid+1
    else:
        end = mid-1
print(end)