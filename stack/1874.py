N = int(input())
temp = True
num = 1
answer = []
stack = []
for i in range(N):
    a = int(input())
    while num <= a:
        stack.append(num)
        answer.append('+')
        num+=1
    if stack[-1] == a:
        stack.pop()
        answer.append('-')
    else:
        temp = False

if temp == False:
    print('NO')
else:
    for i in answer:
        print(i)
# 예외처리 할 때 temp의 참 거짓으로 활용!!!!  복습무조건 해라