import sys

read = lambda: sys.stdin.readline().rstrip()

T = int(read())

for _ in range(T):
    floor = int(read())
    num = int(read())

    f_list = [i for i in range(1, num+1)]

    for i in range(floor):
        for j in range(1, num):
            f_list[j] += f_list[j-1]

    print(f_list[-1])
