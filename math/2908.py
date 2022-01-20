A, B = map(list, input().split())
list_a = list(map(int, A))
list_b = list(map(int, B))
a = []
b = []
for i in range(2, -1, -1):
    a.append(list_a[i])
    b.append(list_b[i])
num_a = a[0]*100 + a[1]*10 + a[2]
num_b = b[0]*100 + b[1]*10 + b[2]
if num_a > num_b:
    print(num_a)
else:
    print(num_b)