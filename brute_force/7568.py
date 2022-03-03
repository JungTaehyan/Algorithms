N = int(input())
a=[]
num = []
for _ in range(N):
    x, y = map(int, input().split())
    a.append((x,y))

for i in a:
    k = 1
    for j in a:
        if i[0]<j[0] and i[1]<j[1]:
            k+=1
    num.append(k)
for i in num:
    print(i)