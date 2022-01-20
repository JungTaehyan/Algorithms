a, b, c, d, e = map(int, input().split())
list_1 = [a, b, c, d, e]
x = 0
for i in list_1:
    x += i**2
print(x%10)