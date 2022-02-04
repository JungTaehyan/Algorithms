A, B, C, D = map(int, input().split())
A_C = C-A
B_D = D-B
list_1 = []
list_1.append(A)
list_1.append(B)
list_1.append(A_C)
list_1.append(B_D)
print(min(list_1))