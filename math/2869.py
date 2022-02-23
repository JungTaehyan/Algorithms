import sys
import math
A, B, V = map(int, sys.stdin.readline().split())
cnt = (V-B)/(A-B)
print(math.ceil(cnt))
# 올림: math.ceil(~)
# 내림 : math.floor(값)
# 반올림 : round(값, 소수점)