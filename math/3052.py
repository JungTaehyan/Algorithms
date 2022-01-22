n = 0
num_list = []
rest_list = []
while n < 10:
    a = int(input())
    num_list.append(a)
    n += 1
for i in range(len(num_list)):
    b = num_list[i] % 42
    rest_list.append(b)
rest_list = set(rest_list)
print(len(rest_list))