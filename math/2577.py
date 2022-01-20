A = int(input())
B = int(input())
C = int(input())
total = A*B*C
total = str(total)
for i in range(0, 10):
    print(total.count(str(i)))
