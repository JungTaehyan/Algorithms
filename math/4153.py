while True:
    a = list(map(int, input().split()))
    a = sorted(a)
    if sum(a) == 0:
        break
    elif a[0]**2 + a[1]**2 == a[2]**2:
        print('right')
    else:
        print('wrong')