T = int(input())
i = 0
while i < T:
    R, S = map(str, input().split())
    i += 1
    a = ""
    for j in range(len(S)):
        a += S[j] * int(R)
    print(a)
