N = int(input())
b = N
for i in range(1, N+1):
    b -= 1
    a = " "*b
    c = "*"*i
    print(a + c)

# print(a, c)이런식으로 하면 중간에 공백이 생김, 그래서 틀림
