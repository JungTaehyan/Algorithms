N = int(input())
num = input()
num_list = list(num.replace("", " ").split())
num_list = list(map(int, num_list))
total = 0
for i in range(N):
    total = total + num_list[i]
print(total)
