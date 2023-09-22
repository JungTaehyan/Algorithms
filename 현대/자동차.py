import sys
car_list = []
n, q = map(int, sys.stdin.readline().split())
car_list = list(map(int,sys.stdin.readline().split()))
car_list.sort()

def search(n, t, car_list):
    l = 0
    r = n-1
    m = n//2
    while True:
        if car_list[m] > t:
            r = m-1
            m = r//2
        elif car_list[m] < t:
            l = m+1
            m = (r+l)//2
        elif car_list[m] == t:
            break
        if r < l or l >= n:
            m=0
            break
    return m

for i in range(q):
    t = int(input())
    v = search(n, t, car_list)
    answer = v*(n-v-1)
    print(answer)


# car_list2 = dict()

# for i in range(n):
#     car_list2[car_list[i]] = i
# for i in range(q):
#     t = int(input())
#     if t not in car_list2:
#         print(0)
#     else:
#         if car_list2[t] == n-1:
#             print(0)
#         else:
#             print(car_list2[t]*(n - (car_list2[t]+1)))