N = int(input())
answer = []
num = 1
while num<=N:
    generator = 0
    total = 0
    str_num = str(num)
    for i in range(len(str_num)):
        generator += int(str_num[i])
    total = generator + num
    if total == N:
        answer.append(num)
    num+=1

if answer == []:
    print('0')
else:
    print(min(answer))
