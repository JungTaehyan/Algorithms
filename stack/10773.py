from sys import stdin
K = int(stdin.readline().strip())
cnt=0
list_1=[]
while cnt < K:
    N = int(stdin.readline().strip())
    if N != 0:
        list_1.append(N)
    elif N==0:
        list_1.pop()
    cnt+=1
print(sum(list_1))