from sys import stdin
N = int(stdin.readline().strip())
n = 0
a = []
while n < N:
    b = int(stdin.readline().strip())
    a.append(b)
    n+=1
a = sorted(a)
for i in a:
    print(i)