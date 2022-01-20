a = []
i = 0
while i<9:
    b = int(input())
    a.append(b)
    i+=1
print(max(a))
print(int(a.index(max(a))+1))