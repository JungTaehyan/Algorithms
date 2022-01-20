A, B = map(int, input().split())
if B >= 45:
    B -= 45
elif A==0 and B < 45:
    A = 23
    B = 60 - 45 + B
else:
    A -= 1
    B = 60 - 45 + B
print(A, B)