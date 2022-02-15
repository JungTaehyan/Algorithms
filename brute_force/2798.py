from sys import stdin
N, M = map(int, stdin.readline().split())
card = list(map(int, stdin.readline().split()))
n = 0
answer = []
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            a = card[i] + card[j] + card[k]
            if a<=M:
                answer.append(a)
print(max(answer))