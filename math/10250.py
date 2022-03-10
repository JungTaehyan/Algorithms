from sys import stdin
T = int(stdin.readline().strip())
cnt=0
while cnt<T:
    list_1 = []
    H, W, N = map(int, stdin.readline().split())
    for i in range(1, W+1):
        for j in range(1, H+1):
            j=str(j)
            if i < 10:
                t=str(0)+str(i)
            else:
                t=str(i)
            list_1.append(j+t)
    N=int(N)
    print(list_1[N-1])
    cnt+=1