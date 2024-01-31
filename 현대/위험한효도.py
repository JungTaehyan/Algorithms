import sys
a, b, d = map(int, sys.stdin.readline().split())
result = 0
tuch = 0
d1 = d

if d <= a and d <= b:
    print(d*2)
elif d <= a and d > b:
    result += (d+b+a)
    d1 = d1 - b
    while True:
        if d1 > b:
            result += (b+a)
            d1 = d1 - b
        elif d1 <= b:
            result += d1
            print(result)
            break
else:
    if d%a == 0 and d%b == 0:
        result = ((a*(d//a)) + (b*(d//a))) + ((b*(d//b))+(a*(d//b)-a))
        print(result)
    elif d%a > 0 and d%b == 0:
        result = (a*(d//a)+d%a) + (b*(d//a)) + ((b*(d//b))+(a*(d//b)-a))
    elif d%a == 0 and d%b > 0:
        result = ((a*(d//a)) + (b*(d//a))) + ((b*(d//b)+d%b)+(a*(d//b)))
    elif d%a > 0 and d%b > 0:
        result = (a*(d//a)+d%a) + (b*(d//a)) + ((b*(d//b)+d%b)+(a*(d//b)))
        
    print(result)