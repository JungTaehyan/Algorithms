N, M = map(int, input().split())
a = 0
chess_w = []
chess_b = []
for i in range(M):
    if i % 2 == 0:
        chess_w.append('W')
    else:
        chess_w.append('B')
for j in range(M):
    if j % 2 == 0:
        chess_b.append('B')
    else:
        chess_b.append('W')
cnt = 0
total_1 =0
total_2 =0
total_list = []
while a < N:
    block = input().replace("", " ").split()
    block.append(cnt)
    if block[M]%2==0 and a <= 8:
        for i in range(8):
            if block[i] != chess_w[i]:
                total_1+=1
            if block[i] != chess_b[i]:
                total_2+=1
    elif block[M]%2==1 and a <= 8:
        for j in range(8):
            if block[j] != chess_b[j]:
                total_1+=1
            if block[j] != chess_w[j]:
                total_2+=1
    a+=1
    cnt+=1

total_list.append(total_1)
total_list.append(total_2)
print(total_1, total_2)



# 보류 개어려움


