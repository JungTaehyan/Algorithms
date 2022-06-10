from sys import stdin
N, K = map(int, stdin.readline().split())
num1 = 1
num2 = 1
num3 = 1
for i in range(1, N+1):
    num1 = i*num1
for j in range(1, K+1):
    num2 = j*num2
for t in range(1, (N-K)+1):
    num3 = t*num3
answer = int(num1/(num2*num3))
print(answer)
# print(N, K)