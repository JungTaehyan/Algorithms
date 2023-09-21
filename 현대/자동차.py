import sys

car_list = []
n, q = map(int, sys.stdin.readline().split())
car_list = list(map(int,sys.stdin.readline().split()))
car_list.sort()
for i in range(q):
    t = int(input())
    if t not in car_list:
        print(0)
    else:
        print(len(car_list[0:car_list.index(t)])*len(car_list[car_list.index(t)+1:]))