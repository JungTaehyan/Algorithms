import sys
T = int(sys.stdin.readline().strip())
i = 0
while i < T:
    a = []
    vps = sys.stdin.readline().strip()
    for j in range(len(vps)):
        if vps[j] == '(':
            a.append('(')
        elif vps[j] == ')' and len(a)==0:
            a.append(')')
        elif a[len(a)-1] =='(' and vps[j] == ')':
            a.pop()
    if len(a) == 0:
        print('YES')
    else:
        print('NO')
    i+=1